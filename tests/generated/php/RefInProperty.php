
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