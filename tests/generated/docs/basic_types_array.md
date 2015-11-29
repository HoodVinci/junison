***

# basic_types_array

***

## Description
> **arrays of basic type**

***

## Heritage


***

## Champs de basic_types_array

Classe |Type | Nom | Description
--|---|---|---
[basic_types_array](basic_types_array.md)|List of integer |integer_array|basic array of integer 
[basic_types_array](basic_types_array.md)|List of boolean |boolean_array|boolean array of boolean 
[basic_types_array](basic_types_array.md)|List of string |string_array|basic array of string 




## Enums Utilisés

## Exemple

```json
{
  "boolean_array": [], 
  "integer_array": [], 
  "string_array": []
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
* arrays of basic type
*/
public class BasicTypesArray  implements Parcelable {

    /************************************************************************
    ** Fields
    ************************************************************************/

    // basic array of integer 
    @SerializedName("integer_array")
    private List<Integer>  integerArray  ;

    // boolean array of boolean 
    @SerializedName("boolean_array")
    private List<Boolean>  booleanArray  ;

    // basic array of string 
    @SerializedName("string_array")
    private List<String>  stringArray  ;


    /************************************************************************
    ** Constructors
    ************************************************************************/

    // No args constructor
    public BasicTypesArray(){}


    /************************************************************************
    ** Getters
    ************************************************************************/

    /**
    * basic array of integer 
    *
    * @return The integerArray
    *
    */
    public List<Integer> getIntegerArray(){
       return integerArray;
    }

    /**
    * boolean array of boolean 
    *
    * @return The booleanArray
    *
    */
    public List<Boolean> getBooleanArray(){
       return booleanArray;
    }

    /**
    * basic array of string 
    *
    * @return The stringArray
    *
    */
    public List<String> getStringArray(){
       return stringArray;
    }




    /************************************************************************
    ** Setters
    ************************************************************************/


    /**
    * @param integerArray
    * basic array of integer 
    */
    public void setIntegerArray(List<Integer>  integerArray){
        this.integerArray = integerArray;
    }

    /**
    * @param booleanArray
    * boolean array of boolean 
    */
    public void setBooleanArray(List<Boolean>  booleanArray){
        this.booleanArray = booleanArray;
    }

    /**
    * @param stringArray
    * basic array of string 
    */
    public void setStringArray(List<String>  stringArray){
        this.stringArray = stringArray;
    }



    /************************************************************************
    ** Parcelable code
    ************************************************************************/



    public final static Parcelable.Creator<BasicTypesArray> CREATOR = new Creator<BasicTypesArray>() {


        public BasicTypesArray createFromParcel(Parcel in) {
            BasicTypesArray instance = new BasicTypesArray();
            in.readList(instance.integerArray, (Integer.class.getClassLoader()));
            in.readList(instance.booleanArray, (Boolean.class.getClassLoader()));
            in.readList(instance.stringArray, (String.class.getClassLoader()));

            return instance;
        }

        public BasicTypesArray[] newArray(int size) {
            return (new BasicTypesArray[size]);
        }

    }



    public void writeToParcel(Parcel dest, int flags) {
            dest.writeList(integerArray)
                    dest.writeList(booleanArray)
                    dest.writeList(stringArray)
            }

    public int describeContents() {
        return  0;
    }




}

```

## Php
```php

<?php
// This file has been auto-generated. Modify it at your own risk


class BasicTypesArray implements JsonSerializable {


    //========================================//
    // ENUMERATION  ARRAYS                    //
    //========================================//



    //========================================//
    // FIELDS DECLARATION                     //
    //========================================//

    // basic array of integer 
    private $integerArray = NULL; // type array
    // boolean array of boolean 
    private $booleanArray = NULL; // type array
    // basic array of string 
    private $stringArray = NULL; // type array

    //========================================//
    // CONSTRUCTORS                           //
    //========================================//


    // Empty constructor
    public function __construct() {}

    //========================================//
    // GETTERS (data is private)              //
    //========================================//

    /**
    * get basic array of integer 
    **/
    public function getIntegerArray() {
        // explicit type cast just to be sure
        return (array) $this->integerArray;
    }

    /**
    * get boolean array of boolean 
    **/
    public function getBooleanArray() {
        // explicit type cast just to be sure
        return (array) $this->booleanArray;
    }

    /**
    * get basic array of string 
    **/
    public function getStringArray() {
        // explicit type cast just to be sure
        return (array) $this->stringArray;
    }


    //========================================//
    // SETTERS (data is private)              //
    //========================================//

    /**
    * set basic array of integer 
    **/
    public function setIntegerArray($integerArray) {
        if (!is_array($integerArray)) {
            trigger_error("Wrong type passed integerArray  is a array" );
            return;
         }
         $this->integerArray = $integerArray ;
    }

    /**
    * set boolean array of boolean 
    **/
    public function setBooleanArray($booleanArray) {
        if (!is_array($booleanArray)) {
            trigger_error("Wrong type passed booleanArray  is a array" );
            return;
         }
         $this->booleanArray = $booleanArray ;
    }

    /**
    * set basic array of string 
    **/
    public function setStringArray($stringArray) {
        if (!is_array($stringArray)) {
            trigger_error("Wrong type passed stringArray  is a array" );
            return;
         }
         $this->stringArray = $stringArray ;
    }



    //========================================//
    // JSON SERIALIZATION                     //
    //========================================//

    public function jsonSerialize() {

        $res = NULL;
        if ((isset($this->integerArray)) and (!empty($this->integerArray))) {
                        $res[integer_array] = $this->getIntegerArray();
            
        }
        if ((isset($this->booleanArray)) and (!empty($this->booleanArray))) {
                        $res[boolean_array] = $this->getBooleanArray();
            
        }
        if ((isset($this->stringArray)) and (!empty($this->stringArray))) {
                        $res[string_array] = $this->getStringArray();
            
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