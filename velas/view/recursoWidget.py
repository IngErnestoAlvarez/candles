from velas.model.recurso.recurso import Recurso
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtWidgets import QMessageBox, QStyle, QStyleOption, QWidget

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
    
    def eliminar(self, button):
        if button.text() == "Cancel": return

        self.rec.eliminar()
        layout = self.parent().layout()
        layout.removeWidget(self)
        layout.update()
        self.setParent(None)
