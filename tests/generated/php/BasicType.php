
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