from PyQt5 import QtCore, QtGui, QtWidgets
from velas.view.uis.uistartingWindow import *


class StartingWindow(QtWidgets.QMainWindow,  Ui_StartingWindow):

    def __init__(self,*args, **kwargs) -> None:
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.actionCrear_recurso.triggered.connect(lambda : self.stackedWidget.setCurrentWidget(self.newRecurso))

        self.button_newRecurso.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.Inicial))

