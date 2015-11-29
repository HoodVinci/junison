
<?php
// This file has been auto-generated. Modify it at your own risk
{% for import in class_.get_imports() %}
include_once "{{import}}";
{% endfor %}


class {{class_.name()}}{% if class_.has_superclass() %} extends {{class_.superclass_name()}}{% endif %} implements JsonSerializable {


    //========================================//
    // ENUMERATION  ARRAYS                    //
    //========================================//
{% for enum in class_.enums %}
     public ${{enum.name()}}PossibleValues = array(
{% for value in enum.items()%}
            "{{value}}",
{% endfor %}
     );

{% endfor %}



    //========================================//
    // FIELDS DECLARATION                     //
    //========================================//

{% for field in class_.fields %}
    // {{field.description()}}
    private ${{field.name()}} = NULL; // type {{field.type()}}
{% endfor %}

    //========================================//
    // CONSTRUCTORS                           //
    //========================================//


    // Empty constructor
    public function __construct() {}

    //========================================//
    // GETTERS (data is private)              //
    //========================================//

{% for field in class_.fields %}
    /**
    * get {{field.description()}}
    **/
    public function {{field.getter_function_name()}}() {
        // explicit type cast just to be sure
{% if  field.is_basic_type() and not field.is_enum() %}
        return ({{field.type()}}) $this->{{field.name()}};
{% else %}
        return $this->{{field.name()}};
{% endif %}
    }

{% endfor %}

    //========================================//
    // SETTERS (data is private)              //
    //========================================//

{% for field in class_.fields %}
    /**
    * set {{field.description()}}
    **/
    public function {{field.setter_function_name()}}({%if not field.is_basic_type()%}{{field.type()}} {% endif %}${{field.name()}}) {
{% if  field.is_basic_type() and not field.is_enum() %}
        if (!{{field.type_check_function()}}(${{field.name()}})) {
            trigger_error("Wrong type passed {{field.name()}}  is a {{field.type()}}" );
            return;
         }
{% elif  field.is_enum() %}
        if (!is_string(${{field.name()}}) && in_array(${{field.name()}},${{field.name()}}PossibleValues)) {
            trigger_error("Wrong value passed value is not in ${{field.name()}}PossibleValues" );
            return;
         }

{% else %}
         if (!(${{field.name()}} instanceof {{field.type()}})) {
            trigger_error( {{field.name()}}.' is  not an instanceof '.{{field.type()}} );
            return;
         }
{% endif %}
         $this->{{field.name()}} = ${{field.name()}} ;
    }

{% endfor %}


    //========================================//
    // JSON SERIALIZATION                     //
    //========================================//

    public function jsonSerialize() {

        $res = NULL;
{% for field in class_.fields %}
        if ((isset($this->{{field.name()}})) and (!empty($this->{{field.name()}}))) {
            {% if field.is_basic_type()%}
            $res[{{field.json_name()}}] = $this->{{field.getter_function_name()}}();
            {% else %}
            $res[{{field.json_name()}}] = $this->{{field.getter_function_name()}}()->jsonSerialize();
            {% endif %}

        }
{% endfor %}

        if (isset($res)){
            $res= array_filter($res, function ($value) {
                return !is_null($value) and !empty($value) && null !=value;
            });
            return $res ;
        }

    }



}




?>