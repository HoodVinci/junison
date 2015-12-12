package {{class_.get_package()}};

/**
* This class has been auto-generated
* Don't modify it. Or do it at your own risk
*/



{% for import in class_.get_imports() %}
import {{import}};
{% endfor %}
import android.os.Parcel;
import android.os.Parcelable;
import android.os.Parcelable.Creator;
import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
* {{class_.description()}}
*/
public class {{class_.name()}} {% if class_.has_superclass() %} extends {{class_.superclass_name()}}{% endif %} implements Parcelable {

    /************************************************************************
    ** Fields
    ************************************************************************/
{% for field in class_.fields %}

    // {{field.description()}}
    @SerializedName("{{field.json_name()}}")
    private {{field.type()}}  {{field.name()}} {%if field.has_default_value() %}= {{field.default_value()}}{% endif %} ;
{% endfor %}


    /************************************************************************
    ** Constructors
    ************************************************************************/

    // No args constructor
    public {{class_.name()}}(){}


    /************************************************************************
    ** Getters
    ************************************************************************/
{% for field in class_.fields %}

    /**
    * {{ field.description()}}
    *
    * @return The {{field.name()}}
    *
    */
    public {{field.type()}} {{field.getter_function_name()}}(){
       return {{field.name()}};
    }
{% endfor %}




    /************************************************************************
    ** Setters
    ************************************************************************/

{% for field in class_.fields %}

    /**
    * @param {{field.name()}}
    * {{field.description()}}
    */
    public void {{field.setter_function_name()}}({{field.type()}}  {{field.name()}}){
        this.{{field.name()}} = {{field.name()}};
    }
{% endfor %}



    /************************************************************************
    ** Parcelable code
    ************************************************************************/



    public final static Parcelable.Creator<{{class_.name()}}> CREATOR = new Creator<{{class_.name()}}>() {


        public {{class_.name()}} createFromParcel(Parcel in) {
            {{class_.name()}} instance = new {{class_.name()}}();
{% for field in class_.fields %}
{% if field.is_list() %}
            in.readList(instance.{{field.name()}}, ({{field.list_type()}}.class.getClassLoader()));
{% else %}
            instance.{{field.name()}}= (({{field.type()}}) in.readValue(({{field.type()}}.class.getClassLoader())));
{% endif %}
{% endfor %}

            return instance;
        }

        public {{class_.name()}}[] newArray(int size) {
            return (new {{class_.name()}}[size]);
        }

    };



    public void writeToParcel(Parcel dest, int flags) {
{% for field in class_.fields %}
{% if field.is_list() %}
    dest.writeList({{field.name()}});
{% else %}
    dest.writeValue({{field.name()}});
{% endif %}
{% endfor %}
    }

    public int describeContents() {
        return  0;
    }



{% for enum in class_.enums%}
/************************************************************************
** Inner enums
************************************************************************/


 public static enum {{enum.name()}} {

{% for id,name in enum.items_with_ids().iteritems()  %}
    @SerializedName("{{id}}") {{name}}("{{id}}"),
{% endfor %} ;
        private final String value;
        private static Map<String, {{class_.name()}}.{{enum.name()}}> constants = new HashMap<String, {{class_.name()}}.{{enum.name()}}>();

        static {
            for ({{class_.name()}}.{{enum.name()}} c: values()) {
                constants.put(c.value, c);
            }
        }

        private {{enum.name()}}(String value) {
            this.value = value;
        }

        @Override
        public String toString() {
            return this.value;
        }

        public static {{class_.name()}}.{{enum.name()}} fromValue(String value) {
            {{class_.name()}}.{{enum.name()}} constant = constants.get(value);
            if (constant == null) {
                throw new IllegalArgumentException(value);
            } else {
                return constant;
            }
        }

    }

{% endfor %}

}

