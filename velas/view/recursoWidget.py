from velas.view.uis.dialogRecurso import Ui_Dialog
from velas.model.recurso.recurso import Recurso
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtWidgets import QBoxLayout, QMessageBox, QStyle, QStyleOption, QWidget

class WidgetRecurso(QtWidgets.QWidget):

    def __init__(self, recurso:Recurso) -> None:
        QtWidgets.QWidget.__init__(self)
        self.rec = recurso
        self.setUp()

        # NOMBRE
        self.nombre = self.crearLabelParaNombre(self.rec.nombre)
        self.layout.addWidget(self.nombre)

        # PRECIO
        self.precio = self.crearLabelParaPrecio(self.rec.precio)
        self.layout.addWidget(self.precio)

        # BOTON DE ELIMINADO
        self.buttonDelete = self.crearBotonDelete()
        self.buttonDelete.clicked.connect(self.messageButtonDelete)
        self.layout.addWidget(self.buttonDelete)

        # BOTON DE AGREGAR STOCK
        self.buttonAdd = self.crearBotonAniadirStock()
        self.buttonAdd.clicked.connect(self.fBotonAniadirStock)
        self.layout.addWidget(self.buttonAdd)
    
    def setUp(self):
        self.setMaximumHeight(50)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.layout.setSpacing(10)

    @staticmethod
    def crearLabelParaNombre(nombre:str) -> QtWidgets.QLabel:
        nombreAux = QtWidgets.QLabel()
        nombreAux.setText(nombre)
        nombreAux.setAccessibleName("widgetRecursoInicio")
        nombreAux.setMaximumWidth(100)
        nombreAux.setToolTip("Nombre del recurso")
        return nombreAux
    
    @staticmethod
    def crearBotonDelete() -> QtWidgets.QPushButton:
        buttonDelete = QtWidgets.QPushButton()
        buttonIcon = QIcon(r"resources\imagenes\basura.png")
        buttonDelete.setIcon(buttonIcon)
        buttonDelete.setMaximumSize(50,50)
        buttonDelete.setAccessibleName("botonBasura")
        buttonDelete.setToolTip("Eliminar recurso")
        return buttonDelete

    @staticmethod
    def crearBotonAniadirStock() -> QtWidgets.QPushButton:
        buttonAddAux = QtWidgets.QPushButton()
        buttonAddIcon = QIcon(r"resources\imagenes\mas.png")
        buttonAddAux.setIcon(buttonAddIcon)
        buttonAddAux.setMaximumSize(50,50)
        buttonAddAux.setAccessibleName("botonBasura")
        buttonAddAux.setToolTip("Añadir stock.")
        return buttonAddAux
    
    @staticmethod
    def crearLabelParaPrecio(precio:float) -> QtWidgets.QLabel:
        precioAux = QtWidgets.QLabel()
        precioAux.setText("$"+str(precio))
        precioAux.setAccessibleName("widgetRecursoInicio")
        precioAux.setMaximumWidth(60)
        precioAux.setToolTip("Precio del recurso")
        precioAux.setStyleSheet("QLabel{font: 16px;}")
        return precioAux


    def cargarEnLayout(self, destino:QBoxLayout) -> None:
        '''Se le pasa como parametro una QBoxLayout y te carga dentro de ella un WidgetRecurso'''
        destino.addWidget(self)
    
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)
    
    def messageButtonDelete(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Esta a punto de eliminar un recurso")
        msg.setInformativeText("Se elminará todo registro de él, incluyendo cantidades y precios.")
        msg.setWindowTitle("Eliminar recurso")
        msg.addButton(QMessageBox.Ok)
        msg.addButton(QMessageBox.Cancel)
        msg.buttonClicked.connect(self.eliminar)

        msg.exec_()
    
    def fBotonAniadirStock(self):
        self.w = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.w)
        self.ui.pushButton.clicked.connect(self.aniadirStock)
        self.w.show()

    def aniadirStock(self):
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
