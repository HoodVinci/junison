import inflection
import os
import json

#
# Utility functions
#

base_type_map = {"string": "string", "integer": "integer", "double": "double",
                 "boolean": "boolean", "number": "float", "any": "object"}

array_type = "List of T "


def class_name_linked(json_class, ref_path):
    if ref_path:
        if ref_path.startswith(".."):
            rel_path = ref_path
        else:
            rel_path = os.path.relpath(ref_path, os.path.dirname(json_class.json_file_path))
    else:
        rel_path = ''
    return create_md_link(title=os.path.basename(rel_path).replace('.json',''), link=rel_path.replace('.json', ''))


def create_md_link(title, link):
    return '[{title}]({link})'.format(title=title, link=link);


def basic_type(json_class, json_type, json_external_ref):
    """
    Handles basic types and simple objects types
    :param json_type:
    :param json_external_ref:
    :return:
    """
    if json_type in base_type_map:
        return base_type_map[json_type]
    elif json_type == 'object':
        if json_external_ref is None:
            raise ValueError("json_external_ref should be set")
        return class_name_linked(json_class, json_external_ref)
    else:
        raise ValueError("precondition not respected")


class MarkdownClassLayer:
    def __init__(self, json_class, php_code, java_code, schemes_path):

        self.php_code = php_code
        self.java_code = java_code
        self.json_class = json_class
        self.schemes_path = schemes_path
        self.fields = []
        self.enums = []
        for json_field in json_class.json_fields:
            self.fields.append(MarkdownFieldLayer(json_field))
            if json_field.is_enum():
                self.enums.append(MarkdownEnumLayer(json_field))
        for json_field in json_class.get_json_inherited_fields():
            self.fields.append(MarkdownFieldLayer(json_field))

    def name(self):
        return self.json_class.json_name

    def get_rel_path(self):
        rel_path = os.path.relpath(self.json_class.json_file_path,self.schemes_path)
        return rel_path

    def description(self):
        return self.json_class.json_description

    def get_exemple_data(self):
        return json.dumps(self.json_class.get_exemple_data(), encoding='utf-8', ensure_ascii=False, sort_keys="True",
                          indent=2)

    def has_superclass(self):
        return self.json_class.json_superclass()

    def superclass_name(self):
        return class_name_linked(self.json_class.json_superclass().json_name)

    def get_imports(self):
        imports = []
        for external in self.json_class.get_json_external_refs():
            name = os.path.basename(external).replace('.json', '')
            imports.append(name)
        return imports

    def get_inheritance_tree(self):
        supers = []
        for super in self.json_class.json_inheritance_tree:
            supers.append(class_name_linked(self.json_class, super.json_file_path))
        return supers


class MarkdownFieldLayer:
    def __init__(self, json_field):
        self.json_field = json_field

    def json_name(self):
        return self.json_field.json_name

    def class_path(self):
        return self.json_class.json_file_path;

    def class_name(self):
        return class_name_linked(self.json_field.json_class, self.json_field.json_external_ref)

    def description(self):
        return self.json_field.json_description

    def is_list(self):
        return self.json_field.is_list()

    def list_type(self):
        json_item_type = self.json_field.json_item_type
        json_external_ref = self.json_field.json_external_ref
        return basic_type(self.json_field.json_class, json_item_type, json_external_ref)

    def type(self):
        is_list = self.json_field.is_list()
        json_type = self.json_field.json_type
        is_enum = self.json_field.is_enum()
        json_external_ref = self.json_field.json_external_ref

        # Check if is enum
        if is_enum:
            # we will create an enum type so the type is the name
            return create_md_link(self.json_field.json_name, '#%s' % self.name())

        # array type
        if is_list:
            return array_type.replace('T', self.list_type())

        return basic_type(self.json_field.json_class, json_type, json_external_ref)

    def name(self):
        return self.json_field.json_name

    def getter_function_name(self):
        return 'get%s' % inflection.camelize(self.json_field.json_name.lower(), True)

    def setter_function_name(self):
        return 'set%s' % inflection.camelize(self.json_field.json_name.lower(), True)

    def default_value(self, json_type, value):
        json_type = self.json_field.json_type
        value = self.json_field.json_default_value
        res = {'string': '"%s"' % value, 'boolean': 'true' if value else 'false', 'integer': value,
               'number': '%sf' % value}
        if json_type in res:
            return res[json_type];
        else:
            return value;

    def has_default_value(self):
        return self.json_field.json_default_value


class MarkdownEnumLayer:
    def __init__(self, json_field):
        self.json_field = json_field

    def name(self):
        return self.json_field.json_name

    def items(self):
        return self.json_field.json_enum_items
