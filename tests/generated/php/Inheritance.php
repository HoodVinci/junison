
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