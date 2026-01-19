import math

def Areaoftriangle():
    #Request user input
    a=float(input("Enter Side a: "))
    b=float(input("Enter Side b: "))
    c=float(input("Enter Side c: "))
    #check if a, b, and c are positive numbers and satisfy the theorem of triangle inequity
    if a > 0 and b >0 and c >0 and a+b>c and a+c>b and b+c>a:
        #calculate triangle's semi perimeter
        s=(a+b+c)/2
        #Calculate triangle's area using Heron's
        area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print(f"The area of the triangle is {area}.")
    else:
        print("A, B, and C must be positive numbers and satisfy the triangle inequity theorem, please press (ENTER) and enter positive numbers")
        #Re-run the function
        Areaoftriangle()
def Areaofcylinder():
    # Request user input
    r = float(input("Enter Radius: "))
    h = float(input("Enter Height: "))
    #check if r and h are not negative numbers
    if r>=0 and h>=0:
        #calculate cylinder's area
        area= 2 * math.pi * r * (r + h)
        print(f"The area of the cylinder is {area}.")
    else:
        print("Radius and Height must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        # Re-run the function
        Areaofcylinder()
def Areaofsphere():
    # Request user input
    r = float(input("Enter Radius: "))
    # check if r is not a negative number
    if r>=0:
        #calculate sphere's area
        area = 4 * math.pi * r**2
        print(f"The area of the sphere is {area}.")
    else:
        print("Radius must not be a negative number, please press (ENTER) and enter a non-negative number")
        # Re-run the function
        Areaofsphere()
def Areaofcircle():
    # Request user input
    r = float(input("Enter Radius: "))
    # check if r is not a negative number
    if r>=0:
        #calculator circle's area
        area=math.pi * r**2
        print(f"The are of the circle is {area}.")
    else:
        print("Radius must not be a negative number, please press (ENTER) and enter a non-negative number")
        #Re-run the function
        Areaofcircle()
def Areaofcuboid():
    # Request user input
    l = float(input("Enter Length: "))
    w = float(input("Enter Width: "))
    h = float(input("Enter height "))
    # check if l, w, and h are not negative numbers
    if l>=0 and w>=0 and h>=0:
        #calculate cuboid's area
        area= 2*(l*w + w*h + h*l)
        print(f"The are of the cuboid is {area}.")
    else:
        print("Length, width, and height must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        #Re-run the function
        Areaofcuboid()
def Areaofrectangle():
    # Request user input
    l = float(input("Enter Length: "))
    w = float(input("Enter Width: "))
    # check if l and w are not negative numbers
    if l>0 and w>0:
        #calculate rectangle's area
        area= l * w
        print(f"The are of the rectangle is {area}.")
    else:
        print("Length and width must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        #Re-run the function
        Areaofrectangle()
def Areaofcube():
    # Request user input
    s = float(input("Enter Side: "))
    # check if s is not a negative number
    if s>=0:
        #calculate cube's area
        area= 6 * s**2
        print(f"The are of the cube is {area}.")
    else:
        print("Side must not be a negative number, please press (ENTER) and enter a non-negative number")
        #Re-run the function
        Areaofcube()
def Areaofsquare():
    # Request user input
    s = float(input("Enter Side: "))
    # check if s is not a negtaive number
    if s>=0:
        #calculate square's area
        area= s**2
        print(f"The are of the square is {area}.")
    else:
        print("Side must not be a negative number, please press (ENTER) and enter a non-negative number")
        #Re-run the function
        Areaofsquare()
def Areaofpyramid():
    # Request user input
    b = float(input("Enter Base: "))
    w = float(input("Enter Width: "))
    s = float(input("Enter Side: "))
    # check if b, w, and s are not negative numbers
    if b>=0 and w>=0 and s>=0:
        #calculate pyramid's base area
        ba= w * b
        #calculate pyramid's lateral area
        la= 2 * (b*s+w*s)
        #calculate pyramid's total area
        ta=la+ba
        print(f"The area of the pyramid is {ta}.")
    else:
        print("Base, width, and side must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        #Re-run the function
        Areaofpyramid()
def Areaofcone():
    # Request user input
    r = float(input("Enter Radius: "))
    h = float(input("Enter Height: "))
    # check if r and h are not negative numbers
    if r>=0 and h>=0:
        #calculate slant height of cone using pythagorean theorem
        s=math.sqrt(r**2+h**2)
        #calculate cone's base area
        ba=math.pi * r**2
        #calculate cone's lateral area
        la=math.pi*r*s
        #calculate cone's total area
        ta=la+ba
        print(f"The area of the cone is {ta}.")
    else:
        print("Radius and height must not be negative numbers, please press (ENTER) and enter non-negative numbers")
        #Re-run the function
        Areaofcone()
def Radiantodegree():
    # Request user input
    ra=float(input("Enter Radian: "))
    # check if ra is not negative
    if ra>= 0:
        #convert radian to degree
        de=math.degrees(ra)
        print(f"The degree conversion of {ra} radian-s is {de} degree-s.")
    else:
        print("Radian must not be negative, please press (ENTER) and enter a non-negative number")
        #re-run the function
        Radiantodegree()
def Degreetoradian():
    # Request user input
    de=float(input("Enter Degree: "))
    # check if de is not negative
    if de>=0:
        #convert degree to radian
        ra=math.radians(de)
        print(f"The radian conversion of {de} degree-s is {ra} radian-s.")
    else:
        print("Degree must not be negative, please press (ENTER) and enter a non-negative number")
        #re-run the function
        Degreetoradian()