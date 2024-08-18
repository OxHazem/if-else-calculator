#main project 50%
import math
import main
import myfunctions
import mh
while True:
    user=input("a-shapes""\tb-trignometric functions""\nc-Quadratic Equations""\td-unit converter""\ne-simple arthimatic calculations" "\twhat would you like to calculate: ")
    if user=="exit":
        break
    elif user.lower()=="a":
        x=input("a-Areas""\tb-volumes""\tc-Lateral areas ")
        if x.lower()=="a":
            import Control
        elif x.lower()=="b":
            x=input("a-cylinder" "\nb-sphere""\nc-cubiod""\nd-cube""\ne-pyramid ""\nf-cone")
            if x.lower()=="a":
                myfunctions.VofCY()
            elif x.lower()=="b":
                myfunctions.VOSP()
            elif x.lower()=="c":
                myfunctions.VOFCU()
            elif x.lower()=="d":
                myfunctions.VOCB()
            elif x.lower()=="e":
                myfunctions.VOFP()
            elif x.lower()=="f":
                myfunctions.VOFCO()
        elif x.lower()=="c":
            x=input("a-the L.A of cone""\t b-the L.A of pyramid""\nc-the L.A of cube""\t d-the L.A of cunbiod""\ne-the L.A of cylinder")
            if x.lower()=="a":
                myfunctions.LATOFCONE()
            elif x.lower()=="b":
                myfunctions.LATOFP()
            elif x.lower()=="c":
                myfunctions.LATOFCUBE()
            elif x.lower()=="d":
                myfunctions.LATOFCUBIOD()
            elif x.lower()=="e":
                myfunctions.LATOFCYLINDER()



    elif user.lower()=="b":
        x=input("a-sin""\tb-cos""\nc-tan""\td-sec""\ne-csc""\tf-cot")
        if x.lower()=="a":
            myfunctions.sin()
        elif x.lower()=="b":
            myfunctions.cos()
        elif x.lower()=="c":
            myfunctions.tan()
        elif x.lower()=="d":
            myfunctions.sec()
        elif x.lower()=="e":
            myfunctions.csc()
        elif x.lower()=="f":
            myfunctions.cot()
    elif user.lower()=="c":
            myfunctions.Qaud()
    elif user.lower()=="d":
        x=input("a-radian to degree ""\tb-degree to radian""\nc-convert to grams" "\td-convert to miligrams""\ne-convert to kiliograms""\tf- convert to tons" "\ng-convert to miliemeter ""\th-convert to centimeter ""\ni- convert to meter""\tj-convert to klometer")
        if x.lower()=="a":
            main.Radiantodegree()
        elif x.lower()=="b":
            main.Degreetoradian()
        elif x.lower()=="c":
            mh.convert_grams()
        elif x.lower()=="d":
            mh.convert_milligrams()
        elif x.lower()=="e":
            mh.convert_kilograms()
        elif x.lower()=="f":
            mh.convert_tons()
        elif x.lower()=="g":
            mh.convert_millimeters()
        elif x.lower()=="h":
            mh.convert_centimeters()
        elif x.lower()=="i":
            mh.convert_meters()
        elif x.lower()=="j":
            mh.convert_kilometers()
    elif user.lower()=="e":
        x=input("a-(+)""\tb-(-)""\tc-(*)""\nd-(/)""\te-(^)")
        if x.lower()=="a":
            mh.add()
        elif x.lower() =="b":
            mh.subtract()
        elif x.lower()=="c":
            mh.multiply()
        elif x.lower()=="d":
            mh.divide()
        elif x.lower()=="e":
            mh.power_function()


