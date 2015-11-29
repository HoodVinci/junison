// This file has been auto-generated. Modify it at your own risk


/**
* {{class_.description()}}
*/
 class {{class_.name()}} {% if class_.has_superclass() %} : {{class_.superclass_name()}}{% endif %}  {

    //======================================================================//
    // Fields
    //======================================================================//

{% for field in class_.fields %}
    // {{field.description()}}
{% if  not field.is_list() %}
    let {{field.name()}} : {{field.type()}} {%if field.has_default_value() %}= {{field.default_value()}}{% endif %} ;
{% else %}
    let  {{field.name()}} = ({{field.list_type()}})[]
{% endif %}
{% endfor %}


    //======================================================================//
    // Initializers
    //======================================================================//

    // No args constructor
    init (json: NSDictionary){

{% for field in class_.fields %}
{% if field.is_basic_type() %}
         if let _{{field.name()}} = json["{{field.json_name()}}"] as? {{field.type()}} {
                self.{{field.name()}} = _{{field.name()}}
            }
{% elif field.is_list() %}
        // list type TODO
{% elif field.is_enum() %}
        // enum type TODO
{% else %}
       // object tpe TODO
{% endif %}


{% endfor %}
    }









    //======================================================================//
    // Inner enums
    //======================================================================//

{% for enum in class_.enums %}

 public  enum {{enum.name()}} : String {

{% for id,name in enum.items_with_ids().iteritems()  %}
    case {{name}} = "{{id}}"
{% endfor %}

{% endfor %}

}

