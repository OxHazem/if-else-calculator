from PySide6.QtWidgets import QMainWindow , QApplication
from PySide6.QtUiTools import QUiLoader
from GUI.code.Conversions import Conversions_page
from GUI.code.Algebra import Algebra_page
from GUI.code.Arithmetic import Arithmetic_page
from GUI.code.Trignometery import Trignometery_page
from GUI.code.Geometery import Geometry_page
loader = QUiLoader() 
class Main_widget(QMainWindow):
    
    def __init__(self): 
        super().__init__()
        self.setWindowTitle("Main Widget")
        self.setGeometry(100, 100, 800, 600)
        self.ui = loader.load("GUI/UI/main.ui", self)
        self.setCentralWidget(self.ui)

        
        

        self.arithmetic_widget = Arithmetic_page()
        self.geometry_widget = Geometry_page()
        self.trig_widget = Trignometery_page()
        self.algebra_widget = Algebra_page()
        self.conversions_widget = Conversions_page()

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
        self.ui.Quit_btn.clicked.connect(self.Quit_App)
        self.ui.show()
    def Quit_App(self):
        QApplication.quit()