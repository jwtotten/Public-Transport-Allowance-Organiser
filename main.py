from pyQT6_UI.landingPage import Ui_Dialog as LandingPageUI
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QFileDialog, QDialog
import subprocess
import sys
from Organiser.Setup import Utils


class LandingPage(QDialog, LandingPageUI):
    def __init__(self) -> None:
        super().__init__()
        self.fileDir = None
        self.setupUi(self)
        self.pushButton.clicked.connect(self.openFileDir)
        self.pushButton_2.clicked.connect(self.sayHi)

    @staticmethod
    @Utils.timefunction
    def sayHi() -> None:
        print('Hi  ')

    def openFileDir(self) -> str:
        fileDir = QFileDialog.getOpenFileName(self, "Open file", "", "")
        print(fileDir[0])
        self.fileDir:str = fileDir[0]
        self.displayOpenedPDF()
        return str(fileDir[0])

    def displayOpenedPDF(self)->None:
        try:
            subprocess.Popen(self.fileDir, shell = True)
        except subprocess.SubprocessError as e:
            raise e


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)

    stackedWidget = LandingPage()
    stackedWidget.show()
    app.exec()



if __name__ == '__main__':
    main()
