# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'novo.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1406, 772)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 8, 1, 1)
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setObjectName("cancelar")
        self.gridLayout.addWidget(self.cancelar, 10, 8, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 8, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 8, 1, 1)
        self.valor_dinheiro = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valor_dinheiro.sizePolicy().hasHeightForWidth())
        self.valor_dinheiro.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.valor_dinheiro.setFont(font)
        self.valor_dinheiro.setObjectName("valor_dinheiro")
        self.gridLayout.addWidget(self.valor_dinheiro, 5, 9, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 3)
        self.excluir = QtWidgets.QPushButton(self.centralwidget)
        self.excluir.setObjectName("excluir")
        self.gridLayout.addWidget(self.excluir, 10, 2, 1, 2)
        self.quantidade = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quantidade.sizePolicy().hasHeightForWidth())
        self.quantidade.setSizePolicy(sizePolicy)
        self.quantidade.setMinimumSize(QtCore.QSize(3, 0))
        self.quantidade.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.quantidade.setFont(font)
        self.quantidade.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.quantidade.setPlaceholderText("")
        self.quantidade.setObjectName("quantidade")
        self.gridLayout.addWidget(self.quantidade, 1, 0, 1, 1)
        self.valor_troco = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valor_troco.sizePolicy().hasHeightForWidth())
        self.valor_troco.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.valor_troco.setFont(font)
        self.valor_troco.setObjectName("valor_troco")
        self.gridLayout.addWidget(self.valor_troco, 8, 9, 1, 1)
        self.pesquisar = QtWidgets.QPushButton(self.centralwidget)
        self.pesquisar.setObjectName("pesquisar")
        self.gridLayout.addWidget(self.pesquisar, 10, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 7, 5, 3)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 8, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 8, 1, 1)
        self.entrada = QtWidgets.QPushButton(self.centralwidget)
        self.entrada.setObjectName("entrada")
        self.gridLayout.addWidget(self.entrada, 0, 4, 1, 1)
        self.valor_cart = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valor_cart.sizePolicy().hasHeightForWidth())
        self.valor_cart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.valor_cart.setFont(font)
        self.valor_cart.setObjectName("valor_cart")
        self.gridLayout.addWidget(self.valor_cart, 6, 9, 1, 1)
        self.lista_vendas = QtWidgets.QTableWidget(self.centralwidget)
        self.lista_vendas.setObjectName("lista_vendas")
        self.lista_vendas.setColumnCount(0)
        self.lista_vendas.setRowCount(0)
        self.gridLayout.addWidget(self.lista_vendas, 3, 0, 7, 7)
        self.relatorio_2 = QtWidgets.QPushButton(self.centralwidget)
        self.relatorio_2.setObjectName("relatorio_2")
        self.gridLayout.addWidget(self.relatorio_2, 10, 9, 1, 1)
        self.relatorio = QtWidgets.QPushButton(self.centralwidget)
        self.relatorio.setObjectName("relatorio")
        self.gridLayout.addWidget(self.relatorio, 10, 4, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)
        self.valor_pix = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valor_pix.sizePolicy().hasHeightForWidth())
        self.valor_pix.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.valor_pix.setFont(font)
        self.valor_pix.setObjectName("valor_pix")
        self.gridLayout.addWidget(self.valor_pix, 7, 9, 1, 1)
        self.pesq_Produt = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pesq_Produt.sizePolicy().hasHeightForWidth())
        self.pesq_Produt.setSizePolicy(sizePolicy)
        self.pesq_Produt.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setPointSize(24)
        
        self.pesq_Produt.setFont(font)
        self.pesq_Produt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pesq_Produt.setText("")
        self.pesq_Produt.setObjectName("pesq_Produt")
        self.pesq_Produt.returnPressed.connect(self.insert_product)

        
        
        self.gridLayout.addWidget(self.pesq_Produt, 1, 2, 1, 1)
        self.valor_total = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valor_total.sizePolicy().hasHeightForWidth())
        self.valor_total.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.valor_total.setFont(font)
        self.valor_total.setReadOnly(True)
        self.valor_total.setObjectName("valor_total")
        self.gridLayout.addWidget(self.valor_total, 9, 9, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 4, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1406, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Total:"))
        self.cancelar.setText(_translate("MainWindow", "F4: Cancelar Venda"))
        self.label_5.setText(_translate("MainWindow", "Troco:"))
        self.label_7.setText(_translate("MainWindow", "Cartão:"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.excluir.setText(_translate("MainWindow", "F3: Excluir"))
        self.quantidade.setText(_translate("MainWindow", "1.00"))
        self.pesquisar.setText(_translate("MainWindow", "F2: Pesquisar"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "Pix:"))
        self.label_8.setText(_translate("MainWindow", "Dinheiro:"))
        self.entrada.setText(_translate("MainWindow", "F1: Entrada/ Saida"))
        self.relatorio_2.setText(_translate("MainWindow", "F1:Finalizar Venda"))
        self.relatorio.setText(_translate("MainWindow", "F5: Relatorio"))
        self.label_2.setText(_translate("MainWindow", "Código/Produto:"))
        self.pesq_Produt.setPlaceholderText(_translate("MainWindow", "Produto"))
        self.label.setText(_translate("MainWindow", "Quantidade:"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Peso:"))