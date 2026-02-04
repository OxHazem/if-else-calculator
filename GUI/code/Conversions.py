from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget 
from conversions.Length import from_centimeters , from_kilometers , from_meters , from_millimeters 
from conversions.weight import from_grams , from_kilograms ,from_milligrams , from_tons
loader = QUiLoader()
class Conversions_page(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("GUI/UI/Conversions.ui",self)
        self.ui.comboBox.currentTextChanged.connect(self.Update_combobox)
        
        

    def Update_combobox(self):
        if self.ui.comboBox.currentText() == "Length":
            self.ui.comboBox_2.addItems(["From Millimeters", "From Centimeters", "From Meters", "From Kilometers"])
        elif self.ui.comboBox.currentText() == "weight":
            self.ui.comboBox_2.addItems(["From Grams", "From Kilograms", "From Milligrams", "From Tons"])
        else:
            self.ui.comboBox_2.clear()
    


        

