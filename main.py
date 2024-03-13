from pyQT6_UI.landingPage import Ui_Dialog as LandingPageUI
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QDialog
import sys


class LandingPage(QDialog, LandingPageUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openFileDir)
        self.pushButton_2.clicked.connect(self.sayHi)


    def sayHi(self) -> None:
        print('Hi')

    def openFileDir(self) -> str:
        fileDir = QFileDialog.getOpenFileName(self, "Open file", "", "")
        print(fileDir[0])
        return str(fileDir[0])


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)

    stackedWidget = LandingPage()
    stackedWidget.show()
    app.exec()



if __name__ == '__main__':
    main()
