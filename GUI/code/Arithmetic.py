from PySide6.QtWidgets import QWidget
from arithmetic.basics import add , subtract , multiply , divide , power 
from PySide6.QtUiTools import QUiLoader
loader = QUiLoader()
class Arithmetic_page(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("GUI/UI/Arithmetic.ui",self)
        self.ui.Add_Button.clicked.connect(self.add_numbers)
        self.ui.Subtract_Button.clicked.connect(self.subtract_numbers)
        self.ui.Multiply_Button.clicked.connect(self.multiply_numbers)
        self.ui.Divide_Button.clicked.connect(self.divide_numbers)
        self.ui.Power_Button.clicked.connect(self.Power)

    def get_numbers(self):
       
        text = self.ui.numbers.toPlainText()
        lines = text.splitlines()

        numbers = []
        for line in lines:
            line = line.strip()
            if line:
                numbers.append(float(line))

        if not numbers:
            raise ValueError("No numbers entered")

        return numbers


    def add_numbers(self):
        try:
            numbers = self.get_numbers()
            result = add(numbers)
            self.ui.Result_Value.setText(str(result))
            self.ui.numbers.clear()
            self.ui.numbers.setPlainText(str(result))
        except Exception:
            self.ui.Result_Value.setText("Error")

    def subtract_numbers(self):
        try:
            numbers = self.get_numbers()
            result = subtract(numbers)
            self.ui.Result_Value.setText(str(result))
            self.ui.numbers.clear()
            self.ui.numbers.setPlainText(str(result))
        except Exception:
            self.ui.Result_Value.setText("Error")

    def multiply_numbers(self):
        try:
            numbers = self.get_numbers()
            result = multiply(numbers)
            self.ui.Result_Value.setText(str(result))
            self.ui.numbers.clear()
            self.ui.numbers.setPlainText(str(result))
        except Exception:
            self.ui.Result_Value.setText("Error")

    def divide_numbers(self):
        try:
            numbers = self.get_numbers()
            result = divide(numbers)
            self.ui.Result_Value.setText(str(result))
            self.ui.numbers.clear()
            self.ui.numbers.setPlainText(str(result))
        except Exception:
            self.ui.Result_Value.setText("Error")



    def Power(self):
        base = self.ui.Base_LineEdit.text()
        exponent = self.ui.Exponent_LineEdit.text()
        try:
            result = power(float(base), float(exponent))
            self.ui.Result_Value.setText(str(result))
            self.ui.numbers.clear()
            self.ui.numbers.setPlainText(str(result))
        except Exception as e:
            self.ui.Result_Value.setText("Error")