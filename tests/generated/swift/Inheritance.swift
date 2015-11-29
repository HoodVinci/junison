// This file has been auto-generated. Modify it at your own risk


/**
* basic inheritance demonstration with the extends value
*/
 class Inheritance  : BasicType  {

    //======================================================================//
    // Fields
    //======================================================================//

    // This is not an inherited attibute
    let myItem : String  ;


    //======================================================================//
    // Initializers
    //======================================================================//

    // No args constructor
    init (json: NSDictionary){

         if let _myItem = json["my_item"] as? String {
                self.myItem = _myItem
            }


    }









    //======================================================================//
    // Inner enums
    //======================================================================//


}
