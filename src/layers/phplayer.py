import inflection
import os

#
# Utility functions
#

base_type_map = {"string": "string", "integer": "int", "double": "float",
                 "boolean": "boolean", "number": "float", "any": "object", "array": "array"}

base_type_function_checks = {"string": "is_string", "integer": "is_int", "boolean": "is_bool", "number": "is_float",
                             "array": "is_array", "double": "is_float"}

array_type = "array"


def class_name(json_name):
    return inflection.camelize(json_name, True)


def basic_type(json_type, json_external_ref):
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
        return class_name(os.path.basename(json_external_ref).replace('.json', ''))
    else:
        raise ValueError("precondition not respected")


class PhpClassLayer:
    def __init__(self, json_class):
        self.json_class = json_class
        self.fields = []

        self.enums = []
        for json_field in json_class.json_fields:
            self.fields.append(PhpFieldLayer(json_field))
            if json_field.is_enum():
                self.enums.append(PhpEnumLayer(json_field))

    def name(self):
        return class_name(self.json_class.json_name)

    def description(self):
        return self.json_class.json_description

    def has_superclass(self):
        return self.json_class.json_superclass()

    def superclass_name(self):
        return class_name(self.json_class.json_superclass().json_name)

    def get_imports(self):
        imports = []
        for external in self.json_class.get_json_external_refs():
            name = class_name(os.path.basename(external).replace('.json', ''))
            imports.append('{0}.{1}'.format(name, 'php'))
        return imports


class PhpFieldLayer:
    def __init__(self, json_field):
        self.json_field = json_field

    def json_name(self):
        return self.json_field.json_name

    def description(self):
        return self.json_field.json_description

    def is_list(self):
        return self.json_field.is_list()

    def is_basic_type(self):
        return self.json_field.json_type in base_type_map and self.json_field.json_type != 'any'

    def type_check_function(self):
        return base_type_function_checks[self.json_field.json_type]

    def list_type(self):
        json_item_type = self.json_field.json_item_type
        json_external_ref = self.json_field.json_external_ref
        return basic_type(json_item_type, json_external_ref)

    def is_enum(self):
        return self.json_field.is_enum()

    def type(self):
        is_list = self.json_field.is_list()
        json_type = self.json_field.json_type
        is_enum = self.json_field.is_enum()
        json_external_ref = self.json_field.json_external_ref

        # Check if is enum
        if is_enum:
            # we will create an enum type so the type is the name
            return class_name(self.json_field.json_name)

        # array type
        if is_list:
            return array_type

        return basic_type(json_type, json_external_ref)

    def name(self):
        return inflection.camelize(self.json_field.json_name.lower(), False)

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


class PhpEnumLayer:
    def __init__(self, json_field):
        self.json_field = json_field

    def name(self):
        return inflection.camelize(self.json_field.json_name.lower(), False)

    def items(self):
        return self.json_field.json_enum_items
