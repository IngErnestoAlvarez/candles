from PyQt5 import QtCore, QtGui, QtWidgets
from velas.view.uis.uistartingWindow import *


class StartingWindow(QtWidgets.QMainWindow,  Ui_StartingWindow):

    signal_newRecurso = QtCore.pyqtSignal(str, float, float)

    def __init__(self,*args, **kwargs) -> None:
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.actionCrear_recurso.triggered.connect(self.factionNewRecurso)

        self.button_newRecurso.clicked.connect(self.fnewRecurso)

    def factionNewRecurso(self):
        self.stackedWidget.setCurrentWidget(self.newRecurso)
        self.lineEdit_nombre_newRecurso.setFocus()

    def fnewRecurso(self):
        self.signal_newRecurso.emit(self.lineEdit_nombre_newRecurso.text(), float(self.lineEdit_precio_newRecurso.text()), float(self.lineEdit_cantidad_newRecurso.text()))
        self.lineEdit_nombre_newRecurso.clear()
        self.stackedWidget.setCurrentWidget(self.Inicial)
