from PySide6.QtUiTools import QUiLoader
loader = QUiLoader()
class Conversions:
    def __init__(self):
        self.ui = loader.load("GUI/UI/Conversions.ui")
        self.ui.setWindowTitle("Conversions")
        self.ui.show()

        

