***

# basic_type

***

## Description
> **None**

***

## Heritage


***

## Champs de basic_type

Classe |Type | Nom | Description
--|---|---|---
[basic_type](basic_type.md)|[enum_field](#enum_field)|enum_field|enum_field
[basic_type](basic_type.md)|integer|boolean_field|boolean field
[basic_type](basic_type.md)|string|integer_field|integer field
[basic_type](basic_type.md)|string|string_field|basic string field




## Enums Utilisés
### enum_field
#### Valeurs possibles
* __value_1__
* __value_2__
* __value_3__
  



## Exemple

```json
{
  "boolean_field": 42, 
  "enum_field": "value_3", 
  "integer_field": "this is a default string", 
  "string_field": "this is a default string"
}
```

## Java
```java

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

```

## Php
```php

<?php
// This file has been auto-generated. Modify it at your own risk


class BasicType implements JsonSerializable {


    //========================================//
    // ENUMERATION  ARRAYS                    //
    //========================================//
     public $enumFieldPossibleValues = array(
            "value_1",
            "value_2",
            "value_3",
     );




    //========================================//
    // FIELDS DECLARATION                     //
    //========================================//

    // enum_field
    private $enumField = NULL; // type EnumField
    // boolean field
    private $booleanField = NULL; // type int
    // integer field
    private $integerField = NULL; // type string
    // basic string field
    private $stringField = NULL; // type string

    //========================================//
    // CONSTRUCTORS                           //
    //========================================//


    // Empty constructor
    public function __construct() {}

    //========================================//
    // GETTERS (data is private)              //
    //========================================//

    /**
    * get enum_field
    **/
    public function getEnumField() {
        // explicit type cast just to be sure
        return $this->enumField;
    }

    /**
    * get boolean field
    **/
    public function getBooleanField() {
        // explicit type cast just to be sure
        return (int) $this->booleanField;
    }

    /**
    * get integer field
    **/
    public function getIntegerField() {
        // explicit type cast just to be sure
        return (string) $this->integerField;
    }

    /**
    * get basic string field
    **/
    public function getStringField() {
        // explicit type cast just to be sure
        return (string) $this->stringField;
    }


    //========================================//
    // SETTERS (data is private)              //
    //========================================//

    /**
    * set enum_field
    **/
    public function setEnumField($enumField) {
        if (!is_string($enumField) && in_array($enumField,$enumFieldPossibleValues)) {
            trigger_error("Wrong value passed value is not in $enumFieldPossibleValues" );
            return;
         }

         $this->enumField = $enumField ;
    }

    /**
    * set boolean field
    **/
    public function setBooleanField($booleanField) {
        if (!is_int($booleanField)) {
            trigger_error("Wrong type passed booleanField  is a int" );
            return;
         }
         $this->booleanField = $booleanField ;
    }

    /**
    * set integer field
    **/
    public function setIntegerField($integerField) {
        if (!is_string($integerField)) {
            trigger_error("Wrong type passed integerField  is a string" );
            return;
         }
         $this->integerField = $integerField ;
    }

    /**
    * set basic string field
    **/
    public function setStringField($stringField) {
        if (!is_string($stringField)) {
            trigger_error("Wrong type passed stringField  is a string" );
            return;
         }
         $this->stringField = $stringField ;
    }



    //========================================//
    // JSON SERIALIZATION                     //
    //========================================//

    public function jsonSerialize() {

        $res = NULL;
        if ((isset($this->enumField)) and (!empty($this->enumField))) {
                        $res[enum_field] = $this->getEnumField();
            
        }
        if ((isset($this->booleanField)) and (!empty($this->booleanField))) {
                        $res[boolean_field] = $this->getBooleanField();
            
        }
        if ((isset($this->integerField)) and (!empty($this->integerField))) {
                        $res[integer_field] = $this->getIntegerField();
            
        }
        if ((isset($this->stringField)) and (!empty($this->stringField))) {
                        $res[string_field] = $this->getStringField();
            
        }

        if (isset($res)){
            $res= array_filter($res, function ($value) {
                return !is_null($value) and !empty($value) && null !=value;
            });
            return $res ;
        }

    }



}




?>
```