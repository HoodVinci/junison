
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
