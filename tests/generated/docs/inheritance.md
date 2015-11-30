***

# inheritance

***

## Description
> **basic inheritance demonstration with the extends value**

***

## Heritage

[basic_type](basic_type.md)  /  
***

## Champs de inheritance

Classe |Type | Nom | Description
--|---|---|---
[inheritance](inheritance.md)|string|my_item|This is not an inherited attibute
[basic_type](basic_type.md)|[enum_field](#enum_field)|enum_field|enum_field
[basic_type](basic_type.md)|integer|boolean_field|boolean field
[basic_type](basic_type.md)|string|integer_field|integer field
[basic_type](basic_type.md)|string|string_field|basic string field




## Enums Utilisés

## Exemple

```json
{
  "boolean_field": 42, 
  "enum_field": "value_3", 
  "integer_field": "this is a default string", 
  "my_item": "this is a default string", 
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

import com.example.test.BasicType;
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
* basic inheritance demonstration with the extends value
*/
public class Inheritance  extends BasicType implements Parcelable {

    /************************************************************************
    ** Fields
    ************************************************************************/

    // This is not an inherited attibute
    @SerializedName("my_item")
    private String  myItem  ;


    /************************************************************************
    ** Constructors
    ************************************************************************/

    // No args constructor
    public Inheritance(){}


    /************************************************************************
    ** Getters
    ************************************************************************/

    /**
    * This is not an inherited attibute
    *
    * @return The myItem
    *
    */
    public String getMyItem(){
       return myItem;
    }




    /************************************************************************
    ** Setters
    ************************************************************************/


    /**
    * @param myItem
    * This is not an inherited attibute
    */
    public void setMyItem(String  myItem){
        this.myItem = myItem;
    }



    /************************************************************************
    ** Parcelable code
    ************************************************************************/



    public final static Parcelable.Creator<Inheritance> CREATOR = new Creator<Inheritance>() {


        public Inheritance createFromParcel(Parcel in) {
            Inheritance instance = new Inheritance();
            instance.myItem= ((String) in.readValue((String.class.getClassLoader())));

            return instance;
        }

        public Inheritance[] newArray(int size) {
            return (new Inheritance[size]);
        }

    }



    public void writeToParcel(Parcel dest, int flags) {
            dest.writeValue(myItem)
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
include_once "BasicType.php";


class Inheritance extends BasicType implements JsonSerializable {


    //========================================//
    // ENUMERATION  ARRAYS                    //
    //========================================//



    //========================================//
    // FIELDS DECLARATION                     //
    //========================================//

    // This is not an inherited attibute
    private $myItem = NULL; // type string

    //========================================//
    // CONSTRUCTORS                           //
    //========================================//


    // Empty constructor
    public function __construct() {}

    //========================================//
    // GETTERS (data is private)              //
    //========================================//

    /**
    * get This is not an inherited attibute
    **/
    public function getMyItem() {
        // explicit type cast just to be sure
        return (string) $this->myItem;
    }


    //========================================//
    // SETTERS (data is private)              //
    //========================================//

    /**
    * set This is not an inherited attibute
    **/
    public function setMyItem($myItem) {
        if (!is_string($myItem)) {
            trigger_error("Wrong type passed myItem  is a string" );
            return;
         }
         $this->myItem = $myItem ;
    }



    //========================================//
    // JSON SERIALIZATION                     //
    //========================================//

    public function jsonSerialize() {

        $res = NULL;
        if ((isset($this->myItem)) and (!empty($this->myItem))) {
                        $res[my_item] = $this->getMyItem();
            
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