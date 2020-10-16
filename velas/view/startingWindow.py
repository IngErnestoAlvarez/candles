from PyQt5.QtWidgets import QSpacerItem
from velas.model.recurso.recurso import cargar
from velas.view.recursoWidget import WidgetRecurso
from PyQt5 import QtCore, QtGui, QtWidgets
from velas.view.uis.uistartingWindow import *


class StartingWindow(QtWidgets.QMainWindow,  Ui_StartingWindow):

    signal_newRecurso = QtCore.pyqtSignal(str, float, float)

    def __init__(self,*args, **kwargs) -> None:
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)


        for rec in cargar():
            recursoAux = WidgetRecurso(rec)
            self.widget_recurso_inicio.layout().addWidget(recursoAux)
        self.widget_recurso_inicio.layout().addStretch()

        self.actionCrear_recurso.triggered.connect(self.factionNewRecurso)
        self.button_newRecurso.clicked.connect(self.fnewRecurso)

    def factionNewRecurso(self):
        self.stackedWidget.setCurrentWidget(self.newRecurso)
        self.lineEdit_nombre_newRecurso.setFocus()

    def fnewRecurso(self):
        self.signal_newRecurso.emit(self.lineEdit_nombre_newRecurso.text(), float(self.lineEdit_precio_newRecurso.text()), float(self.lineEdit_cantidad_newRecurso.text()))
        self.lineEdit_nombre_newRecurso.clear()
        self.lineEdit_cantidad_newRecurso.clear()
        self.lineEdit_precio_newRecurso.clear()
        self.stackedWidget.setCurrentWidget(self.Inicial)
