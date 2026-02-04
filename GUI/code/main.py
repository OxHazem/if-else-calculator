from PySide6.QtWidgets import QApplication
from GUI.code.Main_widget import Main_widget
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main_widget()
    

    sys.exit(app.exec())

