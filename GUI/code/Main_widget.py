from PySide6.QtWidgets import QMainWindow , QApplication
from PySide6.QtUiTools import QUiLoader
loader = QUiLoader() 
class Main_widget(QMainWindow):
    
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Main Widget")
        self.setGeometry(100, 100, 800, 600)
        self.ui = loader.load("GUI/UI/main.ui", self)
        self.setCentralWidget(self.ui)
        

        self.arithmetic_widget = loader.load("GUI/UI/Arithmetic.ui")
        self.geometry_widget = loader.load("GUI/UI/Geometry.ui", self)
        self.trig_widget = loader.load("GUI/UI/Trignometery.ui", self)
        self.algebra_widget = loader.load("GUI/UI/Algebra.ui", self)
        self.conversions_widget = loader.load("GUI/UI/Conversions.ui")

        self.ui.stackedWidget.addWidget(self.arithmetic_widget)
        self.ui.stackedWidget.addWidget(self.geometry_widget)
        self.ui.stackedWidget.addWidget(self.trig_widget)
        self.ui.stackedWidget.addWidget(self.algebra_widget)
        self.ui.stackedWidget.addWidget(self.conversions_widget)



        self.ui.Arithmetic.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.arithmetic_widget))
        self.ui.Geometry.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.geometry_widget))
        self.ui.Trig.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.trig_widget))
        self.ui.Algebra.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.algebra_widget))
        self.ui.Conversions.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.conversions_widget))
        self.ui.show()
        self.ui.Quit_btn.clicked.connect(self.Quit_App)
    def Quit_App(self):
        QApplication.quit()