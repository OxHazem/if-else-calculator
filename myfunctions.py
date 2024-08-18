#volume of cylinder
def VofCY ():
     r   =float(input("the radius = "))
     H=float(input("the height = "))
     pi=3.14
     V=pi*r**2*H
     if r<0 or H<0:
         print("INVALID")
         return (VofCY())
     else:
        print("THE V = "+str(V))

#
#volume of sphere
def VOSP():
    pi=3.14

    R=float(input("the radius is ="))
    V=4/3 *pi*R**3
    if R<0:
             print("INVALID")
             return (VOSP())
    else:
            print("THE V="+str(V))
#volume of cubiod
def VOFCU ():
     length=float(input("the lenghth = "))
     b=' the width is = '
     Width=float(input(b.title()))
     c='the height = '
     Height=float(input(c.title()))
     V=length*Height*Width
     if Height<0 or length<0 or Width<0 :
         print("INVALID")
         return (VOFCU())
     else:
         print("the V = "+ str(V))
#VOLUME OF CUBE
def VOCB():
     a='the Side is = '
     side=float(input(a.title()))
     V=side**3
     if side<0:
         print("INVALID")
         return (VOCB())
     else:
         print("the V= "+str(V))

#volume of pyramid
def VOFP():
     l=float(input("the Lenght is ="))
     w=float(input("the width is = "))
     h=float(input("the height is = "))
     V=(l*w*h)/3
     if l<0 or w<0 or h<0:
         print("INVALID")
         return (VOFP())
     else:
         print("the V= "+str(V))
#VOLUME OF CONE
def VOFCO():
     r=float(input("the radius is = "))
     h=float(input("the height is ="))
     pi=3.14
     V=pi*r**2*(h/3)
     if r<0 or h<0 :
         print("INVALID")
         return (VOFCO())
     else:
         print("the V= " + str(V))
#
#sin
def sin():
     x=int(input("the angle is ="))
     pi=3.14
     rad=(x/180)*pi
     sin02=rad-rad**3/6+rad**5/120-rad**7/5040
     print(f'sin({x})={sin02}')
     return(x)
#cos()
def cos ():
     x=float(input("the angle is = "))
     pi=3.14
     rad=(x/180)*pi
     cos=1-rad**2/2+rad**4/24-rad**6/720
     print("the cosine = "+ str(cos))
     return(x)
#TAN
def tan():
     x=float(input("the angle is ="))
     pi=3.14
     rad=(x/180)*pi
     tan=rad+rad**3/3+(2*rad**5)/15+(17*rad**7)/315
     print("the tan=" + str(tan))
     return(x)
#sec()
def sec():
     x=float(input("the angle is = "))
     pi = 3.14
     rad=(x/180)*pi
     cos=1-rad**2/2+rad**4/24-rad**6/720
     sec=1/cos
     print("the sec = "+str(sec))
     return (x)
#cot()
def cot():
     x=float(input("the angle is ="))
     pi = 3.14
     rad = (x / 180) * pi
     tan = rad + rad ** 3 / 3 + (2 * rad ** 5) / 15 + (17 * rad ** 7) / 315
     cot=1/tan
     print("the cot ="+str(cot))
     return(x)
#csc
def csc():
     x = float(input("the angle is ="))
     pi = 3.14
     rad = (x / 180) * pi
     sin=rad-rad**3/6+rad**5/120-rad**7/5040
     csc=(1/sin)
     print("the csc ="+str(csc))
     return(x)
#L.A
def LATOFCONE():
     r=float(input("THE RADIUS = "))
     h=float(input("THE HEIGHT = "))
     pi=3.14
     A=pi*r*(h**2+r**2)**0.5
     if r<0 or h<0:
           print("INVALID")
           return (r)
     else:
            print("the LATOFCONE is = " +str(A))
#L.A of pyramid
def LATOFP():
     l=float(input("THE LENGTH = " ))
     w=float(input("THE WIDTH = "))
     h=float(input("THE HEIGHT = "))
     A=l*((w/2)**2+(h)**2)**0.5+w*((l/2)**2+h**2)**0.5
     if l<0 or w<0 or h<0:
         print("INVALID")
         return (LATOFP())
     else:
         print("the lat of pyramid is = "+str(A))


def LATOFCUBE():
     x=float(input("the side = "))
     A=4*x**2
     if x<0:
         print("INVALID")
         return (LATOFCUBE())

     else:
         print('the lat of cube is ='+str(A))
#lat of cubiod
def LATOFCUBIOD():
     l=float(input('the length = '))
     h=float(input('the height = '))
     w=float(input('the width = '))
     A=2*h*(l+w)
     if l<0 or h<0 or w<0:
         print("INVALID")
         return (LATOFCUBIOD())
     else:
         print("the LAt of cubiod is ="+str(A))

#lat of cylinder
def LATOFCYLINDER():
     r=float(input("the radius is ="))
     h=float(input("the height is = "))
     pi=3.14
     A=2*pi*r*h
     if r<0 or h<0:
         print("INVALID")
         return (LATOFCYLINDER())
     else:
         print("the lat of  cylinder is ="+str(A))
def Qaud():
    from math import sqrt

    uInput = input("Enter coefficients: ").split()

    a = int(uInput[0])
    b = int(uInput[1])
    c = int(uInput[2])

    if a == 0 and b == 0 and c == 0:
        print("Any x is a solution")
    elif a == 0 and b == 0 and c != 0:
        print("No Solution")
    elif a == 0:
        sol = -c / b
        print(sol)
    else:
        sol = (-b - sqrt((b ** 2) - 4 * a * c)) / (2 * a)
        print(sol)
        sol = (-b + sqrt((b ** 2) - 4 * a * c)) / (2 * a)

        if sol!=0:
            print(sol)
        else:
            print(sol)
            return(Qaud())