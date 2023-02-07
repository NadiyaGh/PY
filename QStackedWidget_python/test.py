import sys
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog,QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow,self).__init__()
        loader = QUiLoader()
        main_window = loader.load("T_main.ui")
        main_window.show()
        main_window.pushButton.clicked.connect(self.gotoScreen2)
        

    def gotoScreen2(self):
        screen2 = Screen2()
        widget.addWidget(screen2)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class Screen2(QDialog):
    def __init__(self):
        super(Screen2,self).__init__()
        loader = QUiLoader()
        main_window = loader.load("T2_main.ui")
        main_window.show()
        main_window.pushButton.clicked.connect(self.gotoScreen1)
        
    def gotoScreen1(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()

try:
    sys.exit(app.exec())
except:
    print("Exiting")
