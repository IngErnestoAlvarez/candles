from PyQt5 import QtWidgets
from velas.view.startingWindow import StartingWindow

class AppController(object):

    def __init__(self, *args, **kwargs) -> None:
        self.app = QtWidgets.QApplication([])
        with open("resources/SpyBot.qss", "r") as file:
            qss = file.read()
            self.app.setStyleSheet(qss)

    def showInicio(self):
        self.window = StartingWindow()
        self.window.show()
        self.app.exec_()
    