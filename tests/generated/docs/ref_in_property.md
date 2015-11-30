***

# ref_in_property

***

## Description
> **basic inheritance demonstration with the extends value**

***

## Heritage


***

## Champs de ref_in_property

Classe |Type | Nom | Description
--|---|---|---
[ref_in_property](ref_in_property.md)|[basic_type](basic_type.md)|external_ref|ref to another class




## Enums Utilisés

## Exemple

```json
{
  "external_ref": {
    "boolean_field": 42, 
    "enum_field": "value_1", 
    "integer_field": "this is a default string", 
    "string_field": "this is a default string"
  }
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
public class RefInProperty  implements Parcelable {

    /************************************************************************
    ** Fields
    ************************************************************************/

    // ref to another class
    @SerializedName("external_ref")
    private BasicType  externalRef  ;


    /************************************************************************
    ** Constructors
    ************************************************************************/

    // No args constructor
    public RefInProperty(){}


    /************************************************************************
    ** Getters
    ************************************************************************/

    /**
    * ref to another class
    *
    * @return The externalRef
    *
    */
    public BasicType getExternalRef(){
       return externalRef;
    }




    /************************************************************************
    ** Setters
    ************************************************************************/


    /**
    * @param externalRef
    * ref to another class
    */
    public void setExternalRef(BasicType  externalRef){
        this.externalRef = externalRef;
    }



    /************************************************************************
    ** Parcelable code
    ************************************************************************/



    public final static Parcelable.Creator<RefInProperty> CREATOR = new Creator<RefInProperty>() {


        public RefInProperty createFromParcel(Parcel in) {
            RefInProperty instance = new RefInProperty();
            instance.externalRef= ((BasicType) in.readValue((BasicType.class.getClassLoader())));

            return instance;
        }

        public RefInProperty[] newArray(int size) {
            return (new RefInProperty[size]);
        }

    }



    public void writeToParcel(Parcel dest, int flags) {
            dest.writeValue(externalRef)
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


class RefInProperty implements JsonSerializable {


    //========================================//
    // ENUMERATION  ARRAYS                    //
    //========================================//



    //========================================//
    // FIELDS DECLARATION                     //
    //========================================//

    // ref to another class
    private $externalRef = NULL; // type BasicType

    //========================================//
    // CONSTRUCTORS                           //
    //========================================//


    // Empty constructor
    public function __construct() {}

    //========================================//
    // GETTERS (data is private)              //
    //========================================//

    /**
    * get ref to another class
    **/
    public function getExternalRef() {
        // explicit type cast just to be sure
        return $this->externalRef;
    }


    //========================================//
    // SETTERS (data is private)              //
    //========================================//

    /**
    * set ref to another class
    **/
    public function setExternalRef(BasicType $externalRef) {
         if (!($externalRef instanceof BasicType)) {
            trigger_error( externalRef.' is  not an instanceof '.BasicType );
            return;
         }
         $this->externalRef = $externalRef ;
    }



    //========================================//
    // JSON SERIALIZATION                     //
    //========================================//

    public function jsonSerialize() {

        $res = NULL;
        if ((isset($this->externalRef)) and (!empty($this->externalRef))) {
                        $res[external_ref] = $this->getExternalRef()->jsonSerialize();
            
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