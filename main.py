# This is a sample Python script.
from pyQT6_UI.landingPage import Ui_Dialog as LandingPageUI
from PyQt6 import QtWidgets
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QWidget, QStackedWidget, QDialog, QMainWindow
import sys
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class LandingPage(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi('pyQT6_UI/landingPage.ui', self)

    def sayHi(self) -> str:
        return "Hi"

def main() -> None:
    app = QtWidgets.QApplication(sys.argv)

    window = LandingPage()
    window.show()
    app.exec()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
