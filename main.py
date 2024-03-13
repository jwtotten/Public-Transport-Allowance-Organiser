# This is a sample Python script.
from pyQT6_UI.landingPage import Ui_Dialog as LandingPageUI
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QStackedWidget, QDialog, QMainWindow
import sys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class LandingPage(QDialog, LandingPageUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.sayHi)


    def sayHi(self) -> None:
        print('Hi')

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)

    stackedWidget = LandingPage()
    stackedWidget.show()
    app.exec()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
