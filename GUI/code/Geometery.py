from PySide6.QtWidgets import QWidget
from geometery.Areas import cube_area ,cuboid_area,circle_area,cylinder_area,sphere_area ,square_area ,rectangle_area ,triangle_area 
from geometery.Lateral_areas import  cone_lateral_area ,pyramid_lateral_area,cube_lateral_area,cuboid_lateral_area,cylinder_lateral_area
from geometery.Volumes import cone_volume ,cube_volume , cuboid_volume , cylinder_volume ,sphere_volume ,pyramid_volume 
from PySide6.QtUiTools import QUiLoader
loader = QUiLoader()
class Geometry_page(QWidget): 
    def __init__(self): 
        super().__init__()
        self.ui = loader.load("GUI/UI/Geometry.ui", self)
        self.ui.comboAreaShape.currentTextChanged.connect(self.Update_inputs_labels)
        self.ui.comboLateralShape.currentTextChanged.connect(self.Update_lateral_area_inputs_labels)
        self.ui.buttonAreaCalculate.clicked.connect(self.calculate_area)
        self.ui.buttonLateralCalculate.clicked.connect(self.calculate_lateral_area)
        self.ui.buttonVolumeCalculate.clicked.connect(self.calculate_volume)
        self.ui.comboVolumeShape.currentTextChanged.connect(self.Update_volume_inputs_labels)
    def show_all_volume_inputs(self):
        self.ui.label_vl1.show()
        self.ui.label_vl2.show()
        self.ui.label_vl3.show()
        self.ui.line_vl_edit1.show()
        self.ui.line_vl_edit2.show()
        self.ui.line_vl_edit3.show()

    def show_lateral_area_inputs(self):
        self.ui.label_la_area1.show()
        self.ui.label_la_area2.show()
        self.ui.label_la_area3.show()
        self.ui.linelaArea1.show()
        self.ui.linelaArea2.show()
        self.ui.linelaArea3.show()
    def show_all(self):
        self.ui.labelAreaInput1.show()
        self.ui.labelAreaInput2.show()
        self.ui.labelAreaInput3.show()
        self.ui.lineEditAreaInput1.show()
        self.ui.lineEditAreaInput2.show()
        self.ui.lineEditAreaInput3.show()


    def calculate_volume(self):
        shape = self.ui.comboVolumeShape.currentText()
    
        if shape == "Cone":
            try:
                radius = float(self.ui.line_vl_edit1.text())
                height = float(self.ui.line_vl_edit2.text())
                volume = cone_volume(radius, height)
                self.ui.label_vl_result.setText(str(volume))
            except ValueError:
                self.ui.label_vl_result.setText("Invalid input")
        elif shape == "Cube":
            try:
                side = float(self.ui.line_vl_edit1.text())
                volume = cube_volume(side)
                self.ui.label_vl_result.setText(str(volume))
            except ValueError:
                self.ui.label_vl_result.setText("Invalid input")
        elif shape == "Cuboid":
            try:
                length = float(self.ui.line_vl_edit1.text())
                width = float(self.ui.line_vl_edit2.text())
                height = float(self.ui.line_vl_edit3.text())
                volume = cuboid_volume(length, width, height)
                self.ui.label_vl_result.setText(str(volume))
            except ValueError:
                self.ui.label_vl_result.setText("Invalid input")
        elif shape == "Cylinder":
            try:
                radius = float(self.ui.line_vl_edit1.text())
                height = float(self.ui.line_vl_edit2.text())
                volume = cylinder_volume(radius, height)
                self.ui.label_vl_result.setText(str(volume))
            except ValueError:
                self.ui.label_vl_result.setText("Invalid input")                
        elif shape == "Sphere":
            try:
                radius = float(self.ui.line_vl_edit1.text())
                volume = sphere_volume(radius)
                self.ui.label_vl_result.setText(str(volume))
            except ValueError:
                self.ui.label_vl_result.setText("Invalid input") 
        elif shape == "Pyramid":
            try: 
                length = float(self.ui.line_vl_edit1.text())
                width = float(self.ui.line_vl_edit2.text())
                height = float(self.ui.line_vl_edit3.text())
                volume = pyramid_volume(length, width, height)
                self.ui.label_vl_result.setText(str(volume))
            except ValueError:
                self.ui.label_vl_result.setText("Invalid input")

    def calculate_lateral_area(self):
            shape = self.ui.comboLateralShape.currentText()

            if shape == "Cone":
                try:
                    radius = float(self.ui.linelaArea1.text())
                    height = float(self.ui.linelaArea2.text())
                    lateral_area = cone_lateral_area(radius, height)
                    self.ui.label_la_result.setText(str(lateral_area))
                except ValueError:
                    self.ui.label_la_result.setText("Invalid input")
            elif shape == "Pyramid":
                try: 
                    length = float(self.ui.linelaArea1.text())
                    width = float(self.ui.linelaArea2.text())
                    height = float(self.ui.linelaArea3.text())
                    lateral_area = pyramid_lateral_area(length, width, height)
                    self.ui.label_la_result.setText(str(lateral_area))
                except ValueError:
                    self.ui.label_la_result.setText("Invalid input")
            elif shape == "Cube":
                try:
                    side = float(self.ui.linelaArea1.text())
                    lateral_area = cube_lateral_area(side)
                    self.ui.label_la_result.setText(str(lateral_area))
                except ValueError:
                    self.ui.label_la_result.setText("Invalid input")
            elif shape == "Cuboid":
                try:
                    length = float(self.ui.linelaArea1.text())
                    width = float(self.ui.linelaArea2.text())
                    height = float(self.ui.linelaArea3.text())
                    lateral_area = cuboid_lateral_area(length, width, height)
                    self.ui.label_la_result.setText(str(lateral_area))
                except ValueError:
                    self.ui.label_la_result.setText("Invalid input")
            elif shape == "Cylinder":
                try:
                    radius = float(self.ui.linelaArea1.text())
                    height = float(self.ui.linelaArea2.text())
                    lateral_area = cylinder_lateral_area(radius, height)
                    self.ui.label_la_result.setText(str(lateral_area))
                except ValueError:
                    self.ui.label_la_result.setText("Invalid input")                

    def calculate_area(self):
        shape = self.ui.comboAreaShape.currentText()

        if shape == "Triangle":
            try:
                a = float(self.ui.lineEditAreaInput1.text())
                b = float(self.ui.lineEditAreaInput2.text())
                c = float(self.ui.lineEditAreaInput3.text())
                area = triangle_area(a, b, c)
                self.ui.labelAreaResult.setText(str(area))
            except ValueError:
                self.ui.labelAreaResult.setText("Invalid input")
        elif shape == "Rectangle":
            try : 
                length = float(self.ui.lineEditAreaInput1.text())
                width = float(self.ui.lineEditAreaInput2.text())
                area = rectangle_area(length, width)
                self.ui.labelAreaResult.setText(str(area))
            except ValueError:
                self.ui.labelAreaResult.setText("Invalid input")
        elif shape == "Square": 
            try:
                side = float(self.ui.lineEditAreaInput1.text())
                area = square_area(side)
                self.ui.labelAreaResult.setText(str(area))
            except ValueError:
                self.ui.labelAreaResult.setText("Invalid input")
        elif shape == "Circle": 
            try:
                radius = float(self.ui.lineEditAreaInput1.text())
                area = circle_area(radius)
                self.ui.labelAreaResult.setText(str(area))
            except ValueError:
                self.ui.labelAreaResult.setText("Invalid input")
        elif shape == "Cube": 
            try:
                side = float(self.ui.lineEditAreaInput1.text())
                area = cube_area(side)
                self.ui.labelAreaResult.setText(str(area))
            except ValueError:
                self.ui.labelAreaResult.setText("Invalid input")
        elif shape == "Cuboid": 
            try:
                length = float(self.ui.lineEditAreaInput1.text())
                width = float(self.ui.lineEditAreaInput2.text())
                height = float(self.ui.lineEditAreaInput3.text())
                area = cuboid_area(length, width, height)
                self.ui.labelAreaResult.setText(str(area))
            except ValueError:
                self.ui.labelAreaResult.setText("Invalid input")
        elif shape == "Cylinder": 
            try:
                radius = float(self.ui.lineEditAreaInput1.text())
                height = float(self.ui.lineEditAreaInput2.text())
                area = cylinder_area(radius, height)
                self.ui.labelAreaResult.setText(str(area))
            except ValueError:
                self.ui.labelAreaResult.setText("Invalid input")
        elif shape == "Sphere": 
            try:
                radius = float(self.ui.lineEditAreaInput1.text())
                area = sphere_area(radius)
                self.ui.labelAreaResult.setText(str(area))
            except ValueError:
                self.ui.labelAreaResult.setText("Invalid input")

    def Update_inputs_labels(self):

        shape =  self.ui.comboAreaShape.currentText()

        if shape == "Triangle":
            self.show_all()
            self.ui.labelAreaInput1.setText("a")
            self.ui.labelAreaInput2.setText("b")
            self.ui.labelAreaInput3.setText("c")
         
        elif shape == "Rectangle":
            self.show_all()
            self.ui.labelAreaInput1.setText("Length")
            self.ui.labelAreaInput2.setText("Width")
            self.ui.labelAreaInput3.hide()
            self.ui.lineEditAreaInput3.hide()
          
        elif shape == "Square": 
            self.show_all()
            self.ui.labelAreaInput1.setText("Side")
            self.ui.labelAreaInput2.hide()
            self.ui.lineEditAreaInput2.hide()
            self.ui.labelAreaInput3.hide()
            self.ui.lineEditAreaInput3.hide()
       
        
        elif shape == "Circle": 
            self.show_all()
            self.ui.labelAreaInput1.setText("Radius")
            self.ui.labelAreaInput2.hide()
            self.ui.labelAreaInput3.hide()
            self.ui.lineEditAreaInput2.hide()
            self.ui.lineEditAreaInput3.hide()
            
        elif shape == "Cube": 
            self.show_all()
            self.ui.labelAreaInput1.setText("Side")
            self.ui.labelAreaInput2.hide()
            self.ui.labelAreaInput3.hide()
            self.ui.lineEditAreaInput2.hide()
            self.ui.lineEditAreaInput3.hide()
           
        elif shape == "Cuboid":
            self.show_all() 
            self.ui.labelAreaInput1.setText("Length")
            self.ui.labelAreaInput2.setText("Width")
            self.ui.labelAreaInput3.setText("Height")
          
        elif shape == "Cylinder": 
            self.show_all()
            self.ui.labelAreaInput1.setText("Radius")
            self.ui.labelAreaInput2.setText("Height")
            self.ui.labelAreaInput3.hide()
            self.ui.lineEditAreaInput3.hide()
          
        elif shape == "Sphere":
            self.show_all() 
            self.ui.labelAreaInput1.setText("Radius")
            self.ui.labelAreaInput2.hide()
            self.ui.labelAreaInput3.hide()
            self.ui.lineEditAreaInput2.hide()
            self.ui.lineEditAreaInput3.hide()
            



    def Update_lateral_area_inputs_labels(self):

        shape = self.ui.comboLateralShape.currentText()


        if shape == "Cone":
            self.show_lateral_area_inputs()
            self.ui.label_la_area1.setText("Radius")
            self.ui.label_la_area2.setText("Height")
            self.ui.label_la_area3.hide()
            self.ui.linelaArea3.hide()
          

        elif shape == "Pyramid":
            self.show_lateral_area_inputs()
            self.ui.label_la_area1.setText("Length")
            self.ui.label_la_area2.setText("Width")
            self.ui.label_la_area3.setText("Height")
         
        elif shape == "Cube":
            self.show_lateral_area_inputs()
            self.ui.label_la_area1.setText("Side")
            self.ui.label_la_area2.hide()
            self.ui.label_la_area3.hide()
            self.ui.linelaArea2.hide()
            self.ui.linelaArea3.hide()
           
        elif shape == "Cuboid":
            self.show_lateral_area_inputs()
            self.ui.label_la_area1.setText("Length")
            self.ui.label_la_area2.setText("Width")
            self.ui.label_la_area3.setText("Height")
          
        elif shape == "Cylinder":
            self.show_lateral_area_inputs()
            self.ui.label_la_area1.setText("Radius")
            self.ui.label_la_area2.setText("Height")
            self.ui.label_la_area3.hide()
            self.ui.linelaArea3.hide()
            
    def Update_volume_inputs_labels(self):
        shape = self.ui.comboVolumeShape.currentText()

        if shape == "Cone":
            self.show_all_volume_inputs()
            self.ui.label_vl1.setText("Radius")
            self.ui.labelvl2.setText("Height")
            self.ui.labelvl3.hide()
            self.ui.line_vl_edit3.hide()
          

        elif shape == "Cube":
            self.show_all_volume_inputs()
            self.ui.label_vl1.setText("Side")
            self.ui.label_vl2.hide()
            self.ui.label_vl3.hide()
            self.ui.line_vl_edit2.hide()
            self.ui.line_vl_edit3.hide()
           
        elif shape == "Cuboid":
            self.show_all_volume_inputs()
            self.ui.label_vl1.setText("Length")
            self.ui.label_vl2.setText("Width")
            self.ui.label_vl3.setText("Height")
          
        elif shape == "Cylinder":
            self.show_all_volume_inputs()
            self.ui.label_vl1.setText("Radius")
            self.ui.label_vl2.setText("Height")
            self.ui.label_vl3.hide()
            self.ui.line_vl_edit3.hide()
            
        elif shape == "Sphere":
            self.show_all_volume_inputs()
            self.ui.label_vl1.setText("Radius")
            self.ui.label_vl2.hide()
            self.ui.label_vl3.hide()
            self.ui.line_vl_edit2.hide()
            self.ui.line_vl_edit3.hide()
            
        elif shape == "Pyramid":
            self.show_all_volume_inputs()
            self.ui.label_vl1.setText("Length")
            self.ui.label_vl2.setText("Width")
            self.ui.label_vl3.setText("Height")
        
        

        
      