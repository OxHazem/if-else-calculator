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
        self.ui.doubleSpinBox.valueChanged.connect(self.Convert)
        self.ui.comboBox_2.currentTextChanged.connect(self.Convert)
        

        
        

    def Update_combobox(self):
        if self.ui.comboBox.currentText() == "Length":
            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.addItems(["From Millimeters", "From Centimeters", "From Meters", "From Kilometers"])
        elif self.ui.comboBox.currentText() == "weight":
            self.ui.comboBox_2.clear()
            self.ui.comboBox_2.addItems(["From Grams", "From Kilograms", "From Milligrams", "From Tons"])
        else:
            self.ui.comboBox_2.clear()
    
    def Convert(self):
        if self.ui.comboBox.currentText() == "Length":
            if self.ui.comboBox_2.currentText() == "From Millimeters":
                result = from_millimeters(self.ui.doubleSpinBox.value())
                self.ui.label_1.setText(f"Millimeters:")
                self.ui.lineEdit_1.setText(f"{result['millimeters']}")

                self.ui.label_2.setText(f"Centimeters:")
                self.ui.lineEdit_2.setText(f"{result['centimeters']}")

                self.ui.label_3.setText(f"Meters:")
                self.ui.lineEdit_3.setText(f"{result['meters']}")

                self.ui.label_4.setText(f"Kilometers:")
                self.ui.lineEdit_4.setText(f"{result['kilometers']}")

            elif self.ui.comboBox_2.currentText() == "From Centimeters":
                result = from_centimeters(self.ui.doubleSpinBox.value())
                self.ui.label_1.setText(f"Millimeters:")
                self.ui.lineEdit_1.setText(f"{result['millimeters']}")

                self.ui.label_2.setText(f"Centimeters:")
                self.ui.lineEdit_2.setText(f"{result['centimeters']}")

                self.ui.label_3.setText(f"Meters:")
                self.ui.lineEdit_3.setText(f"{result['meters']}")

                self.ui.label_4.setText(f"Kilometers:")
                self.ui.lineEdit_4.setText(f"{result['kilometers']}")
            elif self.ui.comboBox_2.currentText() == "From Meters":
                result = from_meters(self.ui.doubleSpinBox.value())
                self.ui.label_1.setText(f"Millimeters:")
                self.ui.lineEdit_1.setText(f"{result['millimeters']}")

                self.ui.label_2.setText(f"Centimeters:")
                self.ui.lineEdit_2.setText(f"{result['centimeters']}")

                self.ui.label_3.setText(f"Meters:")
                self.ui.lineEdit_3.setText(f"{result['meters']}")

                self.ui.label_4.setText(f"Kilometers:")
                self.ui.lineEdit_4.setText(f"{result['kilometers']}")
            elif self.ui.comboBox_2.currentText() == "From Kilometers":
                result = from_kilometers(self.ui.doubleSpinBox.value())
                self.ui.label_1.setText(f"Millimeters:")
                self.ui.lineEdit_1.setText(f"{result['millimeters']}")

                self.ui.label_2.setText(f"Centimeters:")
                self.ui.lineEdit_2.setText(f"{result['centimeters']}")

                self.ui.label_3.setText(f"Meters:")
                self.ui.lineEdit_3.setText(f"{result['meters']}")

                self.ui.label_4.setText(f"Kilometers:")
                self.ui.lineEdit_4.setText(f"{result['kilometers']}")

        elif self.ui.comboBox.currentText() == "weight":
            if self.ui.comboBox_2.currentText() == "From Grams":
                result = from_grams(self.ui.doubleSpinBox.value())
                self.ui.label_1.setText(f"Milligrams:")
                self.ui.lineEdit_1.setText(f"{result['milligrams']}")

                self.ui.label_2.setText(f"Grams:")
                self.ui.lineEdit_2.setText(f"{result['grams']}")

                self.ui.label_3.setText(f"Kilograms:")
                self.ui.lineEdit_3.setText(f"{result['kilograms']}")

                self.ui.label_4.setText(f"Tons:")
                self.ui.lineEdit_4.setText(f"{result['tons']}")
            elif self.ui.comboBox_2.currentText() == "From Kilograms":
                result = from_kilograms(self.ui.doubleSpinBox.value())
                self.ui.label_1.setText(f"Milligrams:")
                self.ui.lineEdit_1.setText(f"{result['milligrams']}")

                self.ui.label_2.setText(f"Grams:")
                self.ui.lineEdit_2.setText(f"{result['grams']}")

                self.ui.label_3.setText(f"Kilograms:")
                self.ui.lineEdit_3.setText(f"{result['kilograms']}")

                self.ui.label_4.setText(f"Tons:")
                self.ui.lineEdit_4.setText(f"{result['tons']}")
            elif self.ui.comboBox_2.currentText() == "From Milligrams":
                result = from_milligrams(self.ui.doubleSpinBox.value())
                self.ui.label_1.setText(f"Milligrams:")
                self.ui.lineEdit_1.setText(f"{result['milligrams']}")

                self.ui.label_2.setText(f"Grams:")
                self.ui.lineEdit_2.setText(f"{result['grams']}")

                self.ui.label_3.setText(f"Kilograms:")
                self.ui.lineEdit_3.setText(f"{result['kilograms']}")

                self.ui.label_4.setText(f"Tons:")
                self.ui.lineEdit_4.setText(f"{result['tons']}")
            elif self.ui.comboBox_2.currentText() == "From Tons":
                result = from_tons(self.ui.doubleSpinBox.value())
                self.ui.label_1.setText(f"Milligrams:")
                self.ui.lineEdit_1.setText(f"{result['milligrams']}")

                self.ui.label_2.setText(f"Grams:")
                self.ui.lineEdit_2.setText(f"{result['grams']}")

                self.ui.label_3.setText(f"Kilograms:")
                self.ui.lineEdit_3.setText(f"{result['kilograms']}")

                self.ui.label_4.setText(f"Tons:")
                self.ui.lineEdit_4.setText(f"{result['tons']}")

        

