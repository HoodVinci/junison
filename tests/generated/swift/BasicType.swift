// This file has been auto-generated. Modify it at your own risk


/**
* None
*/
 class BasicType   {

    //======================================================================//
    // Fields
    //======================================================================//

    // enum_field
    let enumField : EnumField  ;
    // boolean field
    let booleanField : Integer  ;
    // integer field
    let integerField : String  ;
    // basic string field
    let stringField : String  ;


    //======================================================================//
    // Initializers
    //======================================================================//

    // No args constructor
    init (json: NSDictionary){

         if let _enumField = json["enum_field"] as? EnumField {
                self.enumField = _enumField
            }


         if let _booleanField = json["boolean_field"] as? Integer {
                self.booleanField = _booleanField
            }


         if let _integerField = json["integer_field"] as? String {
                self.integerField = _integerField
            }


         if let _stringField = json["string_field"] as? String {
                self.stringField = _stringField
            }


    }









    //======================================================================//
    // Inner enums
    //======================================================================//


 public  enum EnumField : String {

    case Value1 = "value_1"
    case Value3 = "value_3"
    case Value2 = "value_2"


}
