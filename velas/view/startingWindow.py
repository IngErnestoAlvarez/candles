from PyQt5 import QtCore, QtGui, QtWidgets
from velas.view.uis.uistartingWindow import *


class StartingWindow(QtWidgets.QMainWindow,  Ui_StartingWindow):

    signal_newRecurso = QtCore.pyqtSignal(str, float)

    def __init__(self,*args, **kwargs) -> None:
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.actionCrear_recurso.triggered.connect(lambda : self.stackedWidget.setCurrentWidget(self.newRecurso))

        self.button_newRecurso.clicked.connect(self.fnewRecurso)

    def fnewRecurso(self):
        self.signal_newRecurso.emit(self.lineEdit_nombre_newRecurso.text(), 1.0)
        self.lineEdit_nombre_newRecurso.clear()
        self.stackedWidget.setCurrentWidget(self.Inicial)
