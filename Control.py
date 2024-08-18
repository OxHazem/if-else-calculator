import main
print("what would you like to calculate?"
      "(a) Area of Triangle"
      "(b) Area of Cylinder"
      "(c) Area of Sphere"
      "(d) Area of Circle"
      "(e) Area of Cuboid"
      "(f) Area of Rectangle"
      "(g) Area of Cube"
      "(h) Area of Square"
      "(i) Area of Pyramid"
      "(j) Area of Cone"
      "(k) Radian to degree"
      "(l) Degree to Radian")
while True:
      # Request user input
      userinput=input("""what would you like to calculate?
      (a) Area of Triangle
      (b) Area of Cylinder
      (c) Area of Sphere
      (d) Area of Circle
      (e) Area of Cuboid
      (f) Area of Rectangle
      (g) Area of Cube
      (h) Area of Square
      (i) Area of Pyramid
      (j) Area of Cone
      Please select one of the functions listed using one of the designated characters or type 'exit' to end program: """)
      if userinput.lower() =='exit':
            break
      elif userinput.lower() == 'a':
            main.Areaoftriangle()
      elif userinput.lower() == 'b':
            main.Areaofcylinder()
      elif userinput.lower() == 'c':
            main.Areaofsphere()
      elif userinput.lower() == 'd':
            main.Areaofcircle()
      elif userinput.lower() == 'e':
            main.Areaofcuboid()
      elif userinput.lower() == 'f':
            main.Areaofrectangle()
      elif userinput.lower() == 'g':
            main.Areaofcube()
      elif userinput.lower() == 'h':
            main.Areaofsquare()
      elif userinput.lower() == 'i':
            main.Areaofpyramid()
      elif userinput.lower() == 'j':
            main.Areaofcone()