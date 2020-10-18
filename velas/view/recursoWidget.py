from velas.view.uis.dialogRecurso import Ui_Dialog
from velas.model.recurso.recurso import Recurso
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtWidgets import QBoxLayout, QMessageBox, QStyle, QStyleOption, QWidget

class WidgetRecurso(QtWidgets.QWidget):

    def __init__(self, recurso:Recurso) -> None:
        QtWidgets.QWidget.__init__(self)
        self.setMaximumHeight(50)
        self.rec = recurso
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(10)

        self.nombre = QtWidgets.QLabel()
        self.nombre.setText(self.rec.nombre)
        self.nombre.setAccessibleName("widgetRecursoInicio")
        self.nombre.setMaximumWidth(100)
        self.layout.addWidget(self.nombre)

        # BOTON DE ELIMINADO
        self.buttonDelete = QtWidgets.QPushButton()
        buttonIcon = QIcon(r"resources\imagenes\basura.png")
        self.buttonDelete.setIcon(buttonIcon)
        self.buttonDelete.setMaximumSize(50,50)
        self.buttonDelete.setAccessibleName("botonBasura")
        self.buttonDelete.clicked.connect(self.messageButton)
        self.layout.addWidget(self.buttonDelete)

        # BOTON DE AGREGAR STOCK
        self.buttonAdd = QtWidgets.QPushButton()
        buttonAddIcon = QIcon(r"resources\imagenes\mas.png")
        self.buttonAdd.setIcon(buttonAddIcon)
        self.buttonAdd.setMaximumSize(50,50)
        self.buttonAdd.setAccessibleName("botonBasura")
        self.buttonAdd.clicked.connect(self.faddStock)
        self.layout.addWidget(self.buttonAdd)
    
    def cargarEnLayout(self, destino:QBoxLayout) -> None:
        '''Se le pasa como parametro una QBoxLayout y te carga dentro de ella un WidgetRecurso'''
        destino.addWidget(self)
    
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)
    
    def messageButton(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Esta a punto de eliminar un recurso")
        msg.setInformativeText("Se elminará todo registro de él, incluyendo cantidades y precios.")
        msg.setWindowTitle("Eliminar recurso")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(self.eliminar)

        msg.exec_()
    
    def faddStock(self):
        self.w = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.w)
        self.ui.pushButton.clicked.connect(self.fBotonAniadir)
        self.w.show()

    def fBotonAniadir(self):
        aniadido = float(self.ui.lineEdit.text())
        self.rec.agregarStock(aniadido)
        self.rec.guardar()
        self.w.close()

    def eliminar(self, button):
        if button.text() == "Cancel": return

        self.rec.eliminar()
        layout = self.parent().layout()
        layout.removeWidget(self)
        layout.update()
        self.setParent(None)
