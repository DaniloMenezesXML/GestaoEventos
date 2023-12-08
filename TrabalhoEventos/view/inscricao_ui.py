# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inscricao_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_inscricao(object):
    def setupUi(self, inscricao):
        if not inscricao.objectName():
            inscricao.setObjectName(u"inscricao")
        inscricao.resize(699, 615)
        self.verticalLayout_2 = QVBoxLayout(inscricao)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(inscricao)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_email_participante = QLabel(self.widget)
        self.lbl_email_participante.setObjectName(u"lbl_email_participante")

        self.verticalLayout.addWidget(self.lbl_email_participante)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.txt_email_participante = QLineEdit(self.widget)
        self.txt_email_participante.setObjectName(u"txt_email_participante")

        self.horizontalLayout.addWidget(self.txt_email_participante)

        self.btn_consultar = QPushButton(self.widget)
        self.btn_consultar.setObjectName(u"btn_consultar")

        self.horizontalLayout.addWidget(self.btn_consultar)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.lbl_nome_participante = QLabel(self.widget)
        self.lbl_nome_participante.setObjectName(u"lbl_nome_participante")

        self.verticalLayout.addWidget(self.lbl_nome_participante)

        self.txt_nome_participante = QLineEdit(self.widget)
        self.txt_nome_participante.setObjectName(u"txt_nome_participante")

        self.verticalLayout.addWidget(self.txt_nome_participante)

        self.cb_evento = QComboBox(self.widget)
        self.cb_evento.addItem("")
        self.cb_evento.setObjectName(u"cb_evento")

        self.verticalLayout.addWidget(self.cb_evento)

        self.cb_sessao = QComboBox(self.widget)
        self.cb_sessao.addItem("")
        self.cb_sessao.setObjectName(u"cb_sessao")
        self.cb_sessao.setEditable(False)

        self.verticalLayout.addWidget(self.cb_sessao)

        self.tb_sessao = QTableWidget(self.widget)
        if (self.tb_sessao.columnCount() < 4):
            self.tb_sessao.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_sessao.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_sessao.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_sessao.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_sessao.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_sessao.setObjectName(u"tb_sessao")
        self.tb_sessao.horizontalHeader().setDefaultSectionSize(165)

        self.verticalLayout.addWidget(self.tb_sessao)

        self.btn_confirmar = QPushButton(self.widget)
        self.btn_confirmar.setObjectName(u"btn_confirmar")

        self.verticalLayout.addWidget(self.btn_confirmar)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(inscricao)

        QMetaObject.connectSlotsByName(inscricao)
    # setupUi

    def retranslateUi(self, inscricao):
        inscricao.setWindowTitle(QCoreApplication.translate("inscricao", u"Dialog", None))
        self.lbl_email_participante.setText(QCoreApplication.translate("inscricao", u"<html><head/><body><p><span style=\" font-size:12pt;\">E-mail do Participante</span></p></body></html>", None))
        self.btn_consultar.setText(QCoreApplication.translate("inscricao", u"Consultar", None))
        self.lbl_nome_participante.setText(QCoreApplication.translate("inscricao", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome do Participante</span></p></body></html>", None))
        self.cb_evento.setItemText(0, QCoreApplication.translate("inscricao", u"Selecione o Evento", None))

        self.cb_evento.setCurrentText(QCoreApplication.translate("inscricao", u"Selecione o Evento", None))
        self.cb_sessao.setItemText(0, QCoreApplication.translate("inscricao", u"Selecione a Sess\u00e3o", None))

        self.cb_sessao.setCurrentText(QCoreApplication.translate("inscricao", u"Selecione a Sess\u00e3o", None))
        ___qtablewidgetitem = self.tb_sessao.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("inscricao", u"Evento", None));
        ___qtablewidgetitem1 = self.tb_sessao.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("inscricao", u" Palestrante Sess\u00e3o", None));
        ___qtablewidgetitem2 = self.tb_sessao.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("inscricao", u"Tema Sess\u00e3o", None));
        ___qtablewidgetitem3 = self.tb_sessao.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("inscricao", u"Hor\u00e1rio Sess\u00e3o", None));
        self.btn_confirmar.setText(QCoreApplication.translate("inscricao", u"Confirmar", None))
    # retranslateUi

