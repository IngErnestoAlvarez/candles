from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QStyle, QStyleOption

class WidgetRecurso(QtWidgets.QWidget):

    def __init__(self) -> None:
        QtWidgets.QWidget.__init__(self)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)

        self.nombre = QtWidgets.QLabel()
        self.nombre.setText("Cera")

        self.layout.addWidget(self.nombre)
    
    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)