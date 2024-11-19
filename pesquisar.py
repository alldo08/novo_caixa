# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pesquisar.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHeaderView ,QLabel, QLineEdit, QMessageBox,QGridLayout,QSizePolicy,QLayout,QTableWidget,QShortcut, QTableWidgetItem
from PyQt5.QtCore import QCoreApplication, QSize,QMetaObject,Qt


class Ui_pesquisar(object):
    def setupUi(self, pesquisar):
        pesquisar.setObjectName("pesquisar")
        pesquisar.setWindowModality(QtCore.Qt.ApplicationModal)
        pesquisar.resize(706, 516)
        self.widget = QtWidgets.QWidget(pesquisar)
        self.widget.setGeometry(QtCore.QRect(10, 10, 691, 501))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 3)
        self.quantidade = QtWidgets.QLineEdit(self.widget)
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
        self.pesq_Produt = QtWidgets.QLineEdit(self.widget)
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
        self.gridLayout.addWidget(self.pesq_Produt, 1, 1, 1, 3)
        self.pesq_Produt.textChanged.connect(self.filterData)
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 4, 1, 1)
        self.tableView = QtWidgets.QTableWidget(self.widget)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 2, 0, 1, 5)
        self.adicionar_venda = QtWidgets.QPushButton(self.widget)
        self.adicionar_venda.setObjectName("adicionar_venda")
        self.gridLayout.addWidget(self.adicionar_venda, 3, 0, 1, 3)
        self.cancelar_pesquisa = QtWidgets.QPushButton(self.widget)
        self.cancelar_pesquisa.setObjectName("cancelar_pesquisa")
        self.gridLayout.addWidget(self.cancelar_pesquisa, 3, 3, 1, 2)
        self.cancelar_pesquisa.clicked.connect(lambda: self.fechar_janela(pesquisar))


        self.retranslateUi(pesquisar)
        QtCore.QMetaObject.connectSlotsByName(pesquisar)
        pesquisar.setTabOrder(self.pesq_Produt, self.quantidade)
        pesquisar.setTabOrder(self.quantidade, self.cancelar_pesquisa)
        pesquisar.setTabOrder(self.cancelar_pesquisa, self.lineEdit_2)
        pesquisar.setTabOrder(self.lineEdit_2, self.tableView)
        pesquisar.setTabOrder(self.tableView, self.adicionar_venda)

        self.loadData()

    def retranslateUi(self, pesquisar):
        _translate = QtCore.QCoreApplication.translate
        pesquisar.setWindowTitle(_translate("pesquisar", "pesquisar"))
        self.label.setText(_translate("pesquisar", "Quantidade:"))
        self.label_2.setText(_translate("pesquisar", "Código/Produto:"))
        self.quantidade.setText(_translate("pesquisar", "1"))
        self.pesq_Produt.setPlaceholderText(_translate("pesquisar", "Produto"))
        self.lineEdit_2.setPlaceholderText(_translate("pesquisar", "Peso:"))
        self.adicionar_venda.setText(_translate("pesquisar", "Adicionar"))
        self.cancelar_pesquisa.setText(_translate("pesquisar", "Cancelar"))
    
    
    def filterData(self):
        texto_pesquisa = self.pesq_Produt.text().strip().lower()
        linhas_correspondentes = []  # Lista para armazenar linhas correspondentes

        for row in range(self.tableView.rowCount()):
            codigo_item = self.tableView.item(row, 0)  # Coluna "código"
            nome_item = self.tableView.item(row, 1)   # Coluna "nome"

            # Inicializar a relevância da correspondência
            relevancia = None

            # Verificar se o código corresponde
            if codigo_item is not None:
                codigo_text = codigo_item.text().strip().lower()
                if texto_pesquisa == codigo_text:
                    relevancia = 0  # Correspondência exata no código
                elif texto_pesquisa in codigo_text:
                    relevancia = 1  # Contém o texto no código

            # Verificar se o nome corresponde
            if relevancia is None and nome_item is not None:
                nome_text = nome_item.text().strip().lower()
                if texto_pesquisa == nome_text:
                    relevancia = 2  # Correspondência exata no nome
                elif texto_pesquisa in nome_text:
                    relevancia = 3  # Contém o texto no nome

            if relevancia is not None:
                linhas_correspondentes.append((row, relevancia))

        # Ordenar as linhas correspondentes pela relevância
        linhas_correspondentes.sort(key=lambda x: x[1])

        # Exibir apenas as linhas correspondentes, na ordem correta
        for row in range(self.tableView.rowCount()):
            self.tableView.setRowHidden(row, True)  # Esconder todas as linhas inicialmente

        for row, _ in linhas_correspondentes:
            self.tableView.setRowHidden(row, False)  # Mostrar apenas as linhas correspondentes
    
    def loadData(self):
        connection = sqlite3.connect('vendas.db')
        cursor = connection.cursor()

        # Selecione a tabela desejada (substitua 'Produtos' pelo nome correto da tabela)
        cursor.execute("SELECT * FROM produtos")
        dados = cursor.fetchall()

        # Feche a conexão com o banco de dados
        connection.close()

        # Limpe o conteúdo da tabela existente
        self.tableView.setRowCount(0)

        # Defina o número de linhas na tabela
        num_linhas = len(dados)
        if num_linhas > 0:
            num_colunas = len(dados[0])
            self.tableView.setRowCount(num_linhas)
            self.tableView.setColumnCount(num_colunas)

            # Preencha a tabela com os dados
            for linha_idx, linha in enumerate(dados):
                for coluna_idx, valor in enumerate(linha):
                    item = QTableWidgetItem(str(valor))
                    self.tableView.setItem(linha_idx, coluna_idx, item)
                    self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)

                    self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
                    self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
 
                    self.tableView.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)

            # Defina os nomes das colunas
            colunas = [str(coluna[0]) for coluna in cursor.description]
            self.tableView.setHorizontalHeaderLabels(colunas)
    
    def fechar_janela(self, pesquisar):
        print("Janela será fechada")
        pesquisar.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui1 = Ui_pesquisar()
    ui1.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())