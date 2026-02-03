from PySide6.QtWidgets import QApplication
from Main_widget import Main_widget
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Main_widget()
    main_window.show()

    sys.exit(app.exec())

