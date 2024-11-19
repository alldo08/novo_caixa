from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 828)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.excluir = QPushButton(self.centralwidget)
        self.excluir.setObjectName(u"excluir")

        self.gridLayout.addWidget(self.excluir, 10, 2, 1, 1)

        self.valor_pix = QLineEdit(self.centralwidget)
        self.valor_pix.setObjectName(u"valor_pix")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.valor_pix.sizePolicy().hasHeightForWidth())
        self.valor_pix.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(30)
        self.valor_pix.setFont(font)

        self.gridLayout.addWidget(self.valor_pix, 7, 9, 1, 1)

        self.cancelar = QPushButton(self.centralwidget)
        self.cancelar.setObjectName(u"cancelar")

        self.gridLayout.addWidget(self.cancelar, 10, 8, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(22)
        self.label_5.setFont(font1)

        self.gridLayout.addWidget(self.label_5, 8, 8, 1, 1)

        self.entrada = QPushButton(self.centralwidget)
        self.entrada.setObjectName(u"entrada")

        self.gridLayout.addWidget(self.entrada, 0, 4, 1, 2)

        self.valor_dinheiro = QLineEdit(self.centralwidget)
        self.valor_dinheiro.setObjectName(u"valor_dinheiro")
        sizePolicy.setHeightForWidth(self.valor_dinheiro.sizePolicy().hasHeightForWidth())
        self.valor_dinheiro.setSizePolicy(sizePolicy)
        self.valor_dinheiro.setFont(font)

        self.gridLayout.addWidget(self.valor_dinheiro, 5, 9, 1, 1)

        self.valor_cart = QLineEdit(self.centralwidget)
        self.valor_cart.setObjectName(u"valor_cart")
        sizePolicy.setHeightForWidth(self.valor_cart.sizePolicy().hasHeightForWidth())
        self.valor_cart.setSizePolicy(sizePolicy)
        self.valor_cart.setFont(font)

        self.gridLayout.addWidget(self.valor_cart, 6, 9, 1, 1)

        self.pesquisar = QPushButton(self.centralwidget)
        self.pesquisar.setObjectName(u"pesquisar")

        self.gridLayout.addWidget(self.pesquisar, 10, 0, 1, 2)

        self.lista_vendas = QTableWidget(self.centralwidget)
        self.lista_vendas.setObjectName(u"lista_vendas")

        self.gridLayout.addWidget(self.lista_vendas, 3, 0, 7, 7)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(15)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.relatorio = QPushButton(self.centralwidget)
        self.relatorio.setObjectName(u"relatorio")

        self.gridLayout.addWidget(self.relatorio, 10, 4, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 5, 8, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 6, 8, 1, 1)

        self.valor_troco = QLineEdit(self.centralwidget)
        self.valor_troco.setObjectName(u"valor_troco")
        sizePolicy.setHeightForWidth(self.valor_troco.sizePolicy().hasHeightForWidth())
        self.valor_troco.setSizePolicy(sizePolicy)
        self.valor_troco.setFont(font)

        self.gridLayout.addWidget(self.valor_troco, 8, 9, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 7, 8, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout.addWidget(self.label_4, 9, 8, 1, 1)

        self.valor_total = QLineEdit(self.centralwidget)
        self.valor_total.setObjectName(u"valor_total")
        sizePolicy.setHeightForWidth(self.valor_total.sizePolicy().hasHeightForWidth())
        self.valor_total.setSizePolicy(sizePolicy)
        self.valor_total.setFont(font)
        self.valor_total.setReadOnly(True)

        self.gridLayout.addWidget(self.valor_total, 9, 9, 1, 1)

        self.relatorio_2 = QPushButton(self.centralwidget)
        self.relatorio_2.setObjectName(u"relatorio_2")

        self.gridLayout.addWidget(self.relatorio_2, 10, 9, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 7, 5, 3)

        self.pesq_Produt = QLineEdit(self.centralwidget)
        self.pesq_Produt.setObjectName(u"pesq_Produt")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pesq_Produt.sizePolicy().hasHeightForWidth())
        self.pesq_Produt.setSizePolicy(sizePolicy1)
        self.pesq_Produt.setMinimumSize(QSize(400, 0))
        font3 = QFont()
        font3.setPointSize(24)
        self.pesq_Produt.setFont(font3)
        self.pesq_Produt.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.pesq_Produt, 1, 2, 1, 1)

        self.quantidade = QLineEdit(self.centralwidget)
        self.quantidade.setObjectName(u"quantidade")
        sizePolicy1.setHeightForWidth(self.quantidade.sizePolicy().hasHeightForWidth())
        self.quantidade.setSizePolicy(sizePolicy1)
        self.quantidade.setMinimumSize(QSize(3, 0))
        self.quantidade.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setPointSize(28)
        self.quantidade.setFont(font4)
        self.quantidade.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.quantidade, 1, 0, 1, 1)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 3)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.excluir.setText(QCoreApplication.translate("MainWindow", u"F3: Excluir", None))
        self.cancelar.setText(QCoreApplication.translate("MainWindow", u"F4: Cancelar Venda", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Troco:", None))
        self.entrada.setText(QCoreApplication.translate("MainWindow", u"F1: Entrada/ Saida", None))
        self.pesquisar.setText(QCoreApplication.translate("MainWindow", u"F2: Pesquisar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quantidade:", None))
        self.relatorio.setText(QCoreApplication.translate("MainWindow", u"F5: Relatorio", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dinheiro:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Cart\u00e3o:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pix:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.relatorio_2.setText(QCoreApplication.translate("MainWindow", u"F1:Finalizar Venda", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo/Produto:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pesq_Produt.setText("")
        self.pesq_Produt.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Produto", None))
        self.quantidade.setText(QCoreApplication.translate("MainWindow", u"1.00", None))
        self.quantidade.setPlaceholderText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi
