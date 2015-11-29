
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
