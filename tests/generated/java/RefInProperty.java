
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
