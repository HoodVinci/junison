
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