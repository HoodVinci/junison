
/**
* This class has been auto-generated
* Don't modify it. Or do it at your own risk
*/

package com.example.test

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
* None
*/
public class BasicType  implements Parcelable {

    /************************************************************************
    ** Fields
    ************************************************************************/

    // enum_field
    @SerializedName("enum_field")
    private EnumField  enumField  ;

    // boolean field
    @SerializedName("boolean_field")
    private Integer  booleanField  ;

    // integer field
    @SerializedName("integer_field")
    private String  integerField  ;

    // basic string field
    @SerializedName("string_field")
    private String  stringField  ;


    /************************************************************************
    ** Constructors
    ************************************************************************/

    // No args constructor
    public BasicType(){}


    /************************************************************************
    ** Getters
    ************************************************************************/

    /**
    * enum_field
    *
    * @return The enumField
    *
    */
    public EnumField getEnumField(){
       return enumField;
    }

    /**
    * boolean field
    *
    * @return The booleanField
    *
    */
    public Integer getBooleanField(){
       return booleanField;
    }

    /**
    * integer field
    *
    * @return The integerField
    *
    */
    public String getIntegerField(){
       return integerField;
    }

    /**
    * basic string field
    *
    * @return The stringField
    *
    */
    public String getStringField(){
       return stringField;
    }




    /************************************************************************
    ** Setters
    ************************************************************************/


    /**
    * @param enumField
    * enum_field
    */
    public void setEnumField(EnumField  enumField){
        this.enumField = enumField;
    }

    /**
    * @param booleanField
    * boolean field
    */
    public void setBooleanField(Integer  booleanField){
        this.booleanField = booleanField;
    }

    /**
    * @param integerField
    * integer field
    */
    public void setIntegerField(String  integerField){
        this.integerField = integerField;
    }

    /**
    * @param stringField
    * basic string field
    */
    public void setStringField(String  stringField){
        this.stringField = stringField;
    }



    /************************************************************************
    ** Parcelable code
    ************************************************************************/



    public final static Parcelable.Creator<BasicType> CREATOR = new Creator<BasicType>() {


        public BasicType createFromParcel(Parcel in) {
            BasicType instance = new BasicType();
            instance.enumField= ((EnumField) in.readValue((EnumField.class.getClassLoader())));
            instance.booleanField= ((Integer) in.readValue((Integer.class.getClassLoader())));
            instance.integerField= ((String) in.readValue((String.class.getClassLoader())));
            instance.stringField= ((String) in.readValue((String.class.getClassLoader())));

            return instance;
        }

        public BasicType[] newArray(int size) {
            return (new BasicType[size]);
        }

    }



    public void writeToParcel(Parcel dest, int flags) {
            dest.writeValue(enumField)
                    dest.writeValue(booleanField)
                    dest.writeValue(integerField)
                    dest.writeValue(stringField)
            }

    public int describeContents() {
        return  0;
    }



/************************************************************************
** Inner enums
************************************************************************/


 public static enum EnumField {

    @SerializedName("value_1") VALUE_1("value_1"),
    @SerializedName("value_3") VALUE_3("value_3"),
    @SerializedName("value_2") VALUE_2("value_2"),
 ;
        private final String value;
        private static Map<String, BasicType.EnumField> constants = new HashMap<String, BasicType.EnumField>();

        static {
            for (BasicType.EnumField c: values()) {
                constants.put(c.value, c);
            }
        }

        private EnumField(String value) {
            this.value = value;
        }

        @Override
        public String toString() { d
            return this.value;
        }

        public static BasicType.EnumField fromValue(String value) {
            BasicType.EnumField constant = constants.get(value);
            if (constant == null) {
                throw new IllegalArgumentException(value);
            } else {
                return constant;
            }
        }

    }


}
