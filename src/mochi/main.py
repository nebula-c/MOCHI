from PyQt6.QtWidgets import QApplication
from mochi import Mochi_Monitor
import sys

def main():
    app = QApplication(sys.argv)
    # icon_path = resource_path('images/logo1.png')
    # app.setWindowIcon(QIcon(icon_path))
    monitor = Mochi_Monitor.Mochi_Monitor()
    monitor.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()