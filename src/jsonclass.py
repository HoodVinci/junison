from jsonfield import JsonField
import codecs
import json
import os
import copy


class JsonClass:
    """
    Abstraction for the jsons schema file class.

    In charge of parsing the file containing the json_schema file.
    Handles the extends property

    :warning
    """
    # shared instance of already defined classes. To avoid too much instantiations
    already_defined = {}

    def __init__(self, file_path):
        """
        True parsing
        :param file_path:
        :return:
        """
        self.json_file_path = os.path.abspath(file_path)
        self.json_fields = []
        self.json_description = None
        self.json_name = os.path.basename(file_path).replace('.json', '')
        self.json_inheritance_tree = []
        self.json_raw_data =None
        # Once we have set default values, parse true data
        self.parse_json_file(file_path)
        self.already_defined[self.json_file_path] = self
        pass

    def add_class_field(self, json_field):
        """
        :param json_field:
        :type json_field : JsonField
        :return:
        """
        self.json_fields.append(json_field)

    def add_class_field_with(self, json_field_name, json_data):
        """

        :param json_field_name: field name in json schema
        :param json_data: json data
        :type json_field_name : string
        :type json_data : dict
        :return:
        """
        new_field = JsonField(json_name=json_field_name,
                              json_data=json_data, json_class=self)
        self.add_class_field(new_field)

    def parse_json_file(self, json_path):
        with codecs.open(json_path, 'r', 'utf-8') as f:
            class_data = json.load(f);
            self.json_raw_data = class_data
            # get description
            if 'description' in class_data:
                self.json_description = class_data['description']
            # parse properties
            if 'properties' in class_data:
                properties = class_data['properties']
                for json_name, json_data in properties.iteritems():
                    self.add_class_field_with(json_name, json_data)

            # check extends and get superclass infos
            if 'extends' in class_data:
                extends_data = class_data['extends']
                if '$ref' in extends_data:
                    superclass_path = self.get_class_path(extends_data['$ref'])
                    if superclass_path in self.already_defined:
                        superclass = self.already_defined[superclass_path]
                    else:
                        superclass = JsonClass(file_path=superclass_path)

                    self.json_inheritance_tree = copy.deepcopy(superclass.json_inheritance_tree)
                    self.json_inheritance_tree.append(superclass)

    def get_json_inherited_fields(self):
        """

        :return:
        """
        res = []
        for ascendant in reversed(self.json_inheritance_tree):
            res += ascendant.json_fields
        return res


    def get_all_fields(self):
        return self.json_fields + self.get_json_inherited_fields();

    def json_superclass(self):
        """
        :return: the JsonClass that the current class extends
        """
        if self.json_inheritance_tree:
            return self.json_inheritance_tree[len(self.json_inheritance_tree)-1]
        else:
            return None

    def get_json_external_refs(self):
        refs = []
        # add superclass ref
        if self.json_superclass():
            refs.append(self.json_superclass().json_file_path)

        # add fields ref
        for field in self.json_fields:
            if not field.json_external_ref is None:
                refs.append(field.json_external_ref)
        return refs;



    def __str__(self):
        s = 'description %s' % self.json_description
        for json_field in self.json_fields:
            s += str(json_field)
        return s

    def get_exemple_data(self):
        res = {}
        for field in self.json_fields:
            res[field.json_name] = field.get_exemple_data(self)
        for field in self.get_json_inherited_fields():
            res[field.json_name] = field.get_exemple_data(self)
        return res

    def get_class(self, ref):
        """

        :param ref: Relative reference
        :return: The JsonClass which is designated by the relative reference
        :rtype: JsonClass
        """
        path = self.get_class_path(ref);
        print(path)
        print(self.json_file_path)
        if path == self.json_file_path:
            return self
        else:
            return JsonClass(file_path=path)

    def get_class_path(self, ref):
        """
        Merge the current file path with the relative ref
        :param ref:
        :return: A consolidated string representing the file path to the ref

        """
        fileDir = os.path.dirname(os.path.realpath(self.json_file_path))

        filename = os.path.join(fileDir,ref)

        filename= os.path.abspath(os.path.realpath(filename))
        return filename





    def _merge_json_dicts(dictA, dictB):
               return {key: value for (key, value) in (dictA.items() + dictB.items())}


    def get_json_raw_properties(self):
        json_fields_dict={}
        for field in self.get_all_fields():
            json_fields_dict[field.json_name] = field.json_raw_data;
        return json_fields_dict ;

    def get_flat_json_data(self):
        flat_json_data = copy.deepcopy(self.json_raw_data)
        flat_json_data['properties']= self.get_json_raw_properties()
        return flat_json_data
