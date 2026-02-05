from PySide6.QtWidgets import QWidget
from trignometry.trig import degrees_to_radians , radians_to_degrees , sine ,cosecant ,secant ,cosine , cotangent ,tangent 
from PySide6.QtUiTools import QUiLoader
loader = QUiLoader()
class Trignometery_page(QWidget):
    def __init__(self): 
        super().__init__()
        self.ui = loader.load("GUI/UI/Trignometery.ui", self)
        self.ui.buttonCalculate.clicked.connect(self.Calculate)
        self.ui.lineEditAngle.editingFinished.connect(self.convert_to_radians)
        self.ui.lineEditRadians.editingFinished.connect(self.convert_to_degrees)

    
    def convert_to_radians(self):
        try:
            text = self.ui.lineEditAngle.text().strip()
            if not text:
                self.ui.lineEditRadians.clear()
                return

            degrees = float(text)
            radians = degrees_to_radians(degrees)

            self.ui.lineEditRadians.blockSignals(True)
            self.ui.lineEditRadians.setText(f"{radians:.8f}")
            self.ui.lineEditRadians.blockSignals(False)

        except ValueError:
            self.ui.lineEditRadians.setText("Invalid input")


    def convert_to_degrees(self):
        try:
            text = self.ui.lineEditRadians.text().strip()
            if not text:
                self.ui.lineEditAngle.clear()
                return

            radians = float(text)
            degrees = radians_to_degrees(radians)

            self.ui.lineEditAngle.blockSignals(True)
            self.ui.lineEditAngle.setText(f"{degrees:.8f}")
            self.ui.lineEditAngle.blockSignals(False)

        except ValueError:
            self.ui.lineEditAngle.setText("Invalid input")
    
    def Calculate(self):
        try: 
            angle = float(self.ui.lineEditAngle.text())
            sin_result = sine(angle)
            cos_result = cosine(angle)
            tan_result = tangent(angle)
            sec_result = secant(angle)
            cosec_result = cosecant(angle)
            cot_result = cotangent(angle)
            self.ui.labelSinValue.setText(str(sin_result))
            self.ui.labelCosValue.setText(str(cos_result))
            self.ui.labelTanValue.setText(str(tan_result))
            self.ui.labelSecValue.setText(str(sec_result))
            self.ui.labelCscValue.setText(str(cosec_result))
            self.ui.labelCotValue.setText(str(cot_result))
        except ValueError:
            self.ui.labelSinValue.setText("Invalid input")
            self.ui.labelCosValue.setText("Invalid input")
            self.ui.labelTanValue.setText("Invalid input")
            self.ui.labelSecValue.setText("Invalid input")
            self.ui.labelCscValue.setText("Invalid input")
            self.ui.labelCotValue.setText("Invalid input")


