from PyQt5.QtWidgets import QBoxLayout
from velas.model.recurso.recurso import Recurso, cargarRecursoAlSistema
from velas.view.recursoWidget import WidgetRecurso
from PyQt5 import QtCore, QtGui, QtWidgets
from velas.view.uis.uistartingWindow import *


class StartingWindow(QtWidgets.QMainWindow,  Ui_StartingWindow):

    signal_newRecurso = QtCore.pyqtSignal(Recurso)

    def __init__(self,*args, **kwargs) -> None:
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.iniciarWidgetDeRecursos()

        self.conectarAccionesYBotones()

    def iniciarWidgetDeRecursos(self):
        for rec in cargarRecursoAlSistema():
            WidgetRecurso(rec).cargarEnLayout(self.widget_recurso_inicio.layout())
        self.widget_recurso_inicio.layout().setAlignment(QtCore.Qt.AlignTop)


    def conectarAccionesYBotones(self):
        self.actionCrear_recurso.triggered.connect(self.factionCrear_Recurso)
        self.actionInicio.triggered.connect(self.factionVolverInicio)
        self.button_newRecurso.clicked.connect(self.fButton_newRecurso)


    def factionCrear_Recurso(self):
        self.stackedWidget.setCurrentWidget(self.newRecurso)
        self.lineEdit_nombre_newRecurso.setFocus()
    
    def factionVolverInicio(self):
        self.stackedWidget.setCurrentWidget(self.Inicial)


    def fButton_newRecurso(self):
        newRecurso = Recurso(self.lineEdit_nombre_newRecurso.text(), float(self.lineEdit_precio_newRecurso.text()), float(self.lineEdit_cantidad_newRecurso.text()))
        self.signal_newRecurso.emit(newRecurso)

        wrec = WidgetRecurso(newRecurso)
        self.widget_recurso_inicio.layout().addWidget(wrec)
        self.limpiarEspacios()

        self.stackedWidget.setCurrentWidget(self.Inicial)

    def limpiarEspacios(self):
        self.lineEdit_nombre_newRecurso.clear()
        self.lineEdit_cantidad_newRecurso.clear()
        self.lineEdit_precio_newRecurso.clear()

