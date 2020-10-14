# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\velas\view\uis\startingWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartingWindow(object):
    def setupUi(self, StartingWindow):
        StartingWindow.setObjectName("StartingWindow")
        StartingWindow.resize(803, 600)
        StartingWindow.setMinimumSize(QtCore.QSize(800, 600))
        StartingWindow.setMaximumSize(QtCore.QSize(1280, 1024))
        self.centralwidget = QtWidgets.QWidget(StartingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.Inicial = QtWidgets.QWidget()
        self.Inicial.setObjectName("Inicial")
        self.stackedWidget.addWidget(self.Inicial)
        self.newRecurso = QtWidgets.QWidget()
        self.newRecurso.setObjectName("newRecurso")
        self.formLayout = QtWidgets.QFormLayout(self.newRecurso)
        self.formLayout.setObjectName("formLayout")
        self.label_nombre_newRecurso = QtWidgets.QLabel(self.newRecurso)
        self.label_nombre_newRecurso.setMinimumSize(QtCore.QSize(200, 0))
        self.label_nombre_newRecurso.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nombre_newRecurso.setObjectName("label_nombre_newRecurso")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nombre_newRecurso)
        self.lineEdit_nombre_newRecurso = QtWidgets.QLineEdit(self.newRecurso)
        self.lineEdit_nombre_newRecurso.setObjectName("lineEdit_nombre_newRecurso")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nombre_newRecurso)
        self.button_newRecurso = QtWidgets.QPushButton(self.newRecurso)
        self.button_newRecurso.setObjectName("button_newRecurso")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.button_newRecurso)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.stackedWidget.addWidget(self.newRecurso)
        self.verticalLayout.addWidget(self.stackedWidget)
        StartingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartingWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 803, 21))
        self.menubar.setObjectName("menubar")
        self.menuRecursos = QtWidgets.QMenu(self.menubar)
        self.menuRecursos.setObjectName("menuRecursos")
        self.menuProductos = QtWidgets.QMenu(self.menubar)
        self.menuProductos.setObjectName("menuProductos")
        StartingWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartingWindow)
        self.statusbar.setObjectName("statusbar")
        StartingWindow.setStatusBar(self.statusbar)
        self.actionCrear_recurso = QtWidgets.QAction(StartingWindow)
        self.actionCrear_recurso.setObjectName("actionCrear_recurso")
        self.actionEliminar_recurso = QtWidgets.QAction(StartingWindow)
        self.actionEliminar_recurso.setObjectName("actionEliminar_recurso")
        self.actionModificar_recurso = QtWidgets.QAction(StartingWindow)
        self.actionModificar_recurso.setObjectName("actionModificar_recurso")
        self.actionCrear_producto = QtWidgets.QAction(StartingWindow)
        self.actionCrear_producto.setObjectName("actionCrear_producto")
        self.actionEliminar_producto = QtWidgets.QAction(StartingWindow)
        self.actionEliminar_producto.setObjectName("actionEliminar_producto")
        self.menuRecursos.addAction(self.actionCrear_recurso)
        self.menuRecursos.addAction(self.actionEliminar_recurso)
        self.menuRecursos.addAction(self.actionModificar_recurso)
        self.menuProductos.addAction(self.actionCrear_producto)
        self.menuProductos.addAction(self.actionEliminar_producto)
        self.menubar.addAction(self.menuRecursos.menuAction())
        self.menubar.addAction(self.menuProductos.menuAction())

        self.retranslateUi(StartingWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StartingWindow)

    def retranslateUi(self, StartingWindow):
        _translate = QtCore.QCoreApplication.translate
        StartingWindow.setWindowTitle(_translate("StartingWindow", "velas"))
        self.label_nombre_newRecurso.setText(_translate("StartingWindow", "Nombre"))
        self.button_newRecurso.setText(_translate("StartingWindow", "Aceptar"))
        self.menuRecursos.setTitle(_translate("StartingWindow", "Recursos"))
        self.menuProductos.setTitle(_translate("StartingWindow", "Productos"))
        self.actionCrear_recurso.setText(_translate("StartingWindow", "Crear recurso"))
        self.actionEliminar_recurso.setText(_translate("StartingWindow", "Eliminar recurso"))
        self.actionModificar_recurso.setText(_translate("StartingWindow", "Modificar recurso"))
        self.actionCrear_producto.setText(_translate("StartingWindow", "Crear producto"))
        self.actionEliminar_producto.setText(_translate("StartingWindow", "Eliminar producto"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartingWindow = QtWidgets.QMainWindow()
    ui = Ui_StartingWindow()
    ui.setupUi(StartingWindow)
    StartingWindow.show()
    sys.exit(app.exec_())
