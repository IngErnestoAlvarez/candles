from PyQt5 import QtWidgets
from velas.view.startingWindow import StartingWindow
from velas.model.recurso.recurso import Recurso

class AppController(object):

    def __init__(self, *args, **kwargs) -> None:
        self.app = QtWidgets.QApplication([])
        with open("resources/SpyBot.qss", "r") as file:
            qss = file.read()
            self.app.setStyleSheet(qss)

    def showInicio(self):
        self.window = StartingWindow()
        self.cargarSignals()
        self.window.show()
        self.app.exec_()

    def cargarSignals(self):
        self.window.signal_newRecurso.connect(self.newRecurso)

    def newRecurso(self, nombre:str, precio:float) -> None:
        rec = Recurso(nombre, precio)
        rec.guardar()