# gui.py
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


import system


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.disksTable = None
        uic.loadUi("install.ui", self)
        self.stackedWidget.setCurrentIndex(0)

        # сигналы
        self.pushButton.clicked.connect(self.on_install)


    def on_install(self):
        ok = system.check_internet()

        if not ok:
            self.welcomeLabel.setText("Нет интернета")
            return

        self.stackedWidget.setCurrentIndex(1)
        self.diskButton2_1.clicked.connect(self.goto2)

    def goto2(self):
        self.stackedWidget.setCurrentIndex(2)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

