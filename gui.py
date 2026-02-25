# gui.py
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
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
        self.diskButton2_2.clicked.connect(self.goto_disk2)
        self.diskButton2_1.clicked.connect(self.goto_disk2)
        self.diskButton2_2.clicked.connect(self.goto_disk2)
        self.amd_button.clicked.connect(self.goto_drivers)    
        self.intel_button.clicked.connect(self.goto_drivers)
        self.nvidia_button.clicked.connect(self.goto_drivers)
        self.dalee_button.clicked.connect(self.goto_end)


    def goto_disk2(self):
        self.stackedWidget.setCurrentIndex(2)

    def goto_disk3(self):
        self.stackedWidget.setCurrentIndex(4)
    
    def goto_presets(self):
        self.stackedWidget.setCurrentIndex(5)
    
    def goto_drivers(self):
        self.stackedWidget.setCurrentIndex(3)

    def goto_end(self):
        self.stackedWidget.setCurrentIndex(6)
    
        
    
    
        





if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())

