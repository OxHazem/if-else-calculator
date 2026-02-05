from PySide6.QtWidgets import QWidget   
from algebra.quadratic import solve_quadratic
from PySide6.QtUiTools import QUiLoader
loader = QUiLoader()
class Algebra_page(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("GUI/UI/Algebra.ui",self)
        self.ui.buttonSolve.clicked.connect(self.solve_equation)

    def solve_equation(self):
        try:
            a = float(self.ui.lineEditA.text())
            b = float(self.ui.lineEditB.text())
            c = float(self.ui.lineEditC.text())

            status, x1, x2 = solve_quadratic(a, b, c)

            if status == "all_real":
                self.ui.labelX1Value.setText("All real numbers")
                self.ui.labelX2Value.setText("")

            elif status == "no_solution":
                self.ui.labelX1Value.setText("No solution")
                self.ui.labelX2Value.setText("")

            elif status == "linear":
                self.ui.labelX1Value.setText(str(x1))
                self.ui.labelX2Value.setText("")

            elif status == "one_real":
                self.ui.labelX1Value.setText(str(x1))
                self.ui.labelX2Value.setText("")

            else:  
                self.ui.labelX1Value.setText(str(x1))
                self.ui.labelX2Value.setText(str(x2))

        except ValueError:
            self.ui.labelX1Value.setText("Invalid input")
            self.ui.labelX2Value.setText("Invalid input")
