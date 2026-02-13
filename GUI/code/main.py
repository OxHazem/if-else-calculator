from PySide6.QtWidgets import QApplication
from GUI.code.Main_widget import Main_widget
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("GUI/style/Main_widget.qss", "r") as f:
        app.setStyleSheet(f.read())

    main_window = Main_widget()
    
    

    sys.exit(app.exec())

