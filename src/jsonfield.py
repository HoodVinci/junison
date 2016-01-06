import random


class JsonField:
    """
        JsonField is an a abstraction of the field as found on json schemas.

        Handles parsing of the json dict.

        :Example:

        "list_of_another_object": {
             "items": {
                "$ref": "another_object.json",
                "type": "object"
            },
            "type": "array"
         }


    """

    exemple_map = {"string": "this is a default string", "integer": 42, "double": 42.0,
                   "boolean": True, "number": 42.01}

    def __init__(self, json_name, json_data, json_class):
        self.json_raw_data = json_data
        self.json_description = ''
        self.json_name = json_name
        self.json_type = 'any'
        self.json_item_type = None
        self.json_class = json_class
        self.json_default_value = None
        self.json_enum_items = []
        self.json_external_ref = None
        self.has_default_value = False

        # After setting default parse data
        self.parse(json_data)

        pass

    def parse(self, json_data):
        # set description
        if 'description' in json_data:
            self.json_description = json_data['description']
        else:
            self.json_description = self.json_name
        # set type
        if 'type' in json_data:
            self.json_type = json_data['type']
            self.parse_item_type(json_data)

        # parse default_value
        if 'default' in json_data:
            self.has_default_value = True
            self.json_default_value = json_data['default']

        if 'enum' in json_data:
            self.json_enum_items = json_data['enum']

    def parse_item_type(self, json_data):
        if self.json_type == 'array':
            if 'items' in json_data:
                items_data = json_data['items']
                if 'type' in items_data:

                    if '$ref' in items_data:
                        self.json_external_ref = items_data['$ref']
                        self.json_item_type = 'object'

                    elif 'superclass' in items_data:
                        self.json_external_ref = items_data['superclass']
                        self.json_item_type = 'object'

                    elif not items_data['type'] == 'object':
                        self.json_item_type = items_data['type']
                    else:
                        raise ValueError('%s should declare a $ref field ' % self.json_name)

                else:
                    raise ValueError(
                        "items has to declare a field type {0}  Field {1} ".format(self.json_class_name,
                                                                                   self.json_name))
            else:
                raise ValueError("array property should have items field")
        if self.json_type == 'object':
            if '$ref' in json_data:
                self.json_external_ref = json_data['$ref']

            elif 'superclass' in json_data:
                self.json_external_ref = json_data['superclass']
            else:
                raise ValueError(
                    '%s should declare a $ref field put any in type field if you want an undetermined  object' % self.json_name)

    def __str__(self):
        return "description {description} type {type} name {name}".format(description=self.json_description,
                                                                          type=self.json_type, name=self.json_name)

    def is_enum(self):
        return self.json_enum_items

    def is_list(self):
        return self.json_item_type

    def get_exemple_data(self, json_class):
        if self.is_enum():
            return random.choice(self.json_enum_items)

        elif self.is_list():
            # Put two items
            num = random.randint(0, 1);
            res = []
            i = 0
            while i <= num:
                # res.append(self._get_exemple_data(self.json_item_type,self.json_external_ref,json_class))
                i += 1
            return res;
        else:
            return self._get_exemple_data(self.json_type, self.json_external_ref, json_class)

    def _get_exemple_data(self, type, external_ref, json_class):

        if type == 'array':
            raise AttributeError("type should not be array at this point")

        if type in self.exemple_map:
            return self.exemple_map[type]
        else:
            class_ = json_class.get_class(external_ref)
            return class_.get_exemple_data()
