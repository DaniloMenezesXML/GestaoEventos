# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inscricao.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import view.icon
class Ui_inscricao(object):
    def setupUi(self, inscricao):
        if not inscricao.objectName():
            inscricao.setObjectName(u"inscricao")
        inscricao.resize(562, 608)
        self.verticalLayout_2 = QVBoxLayout(inscricao)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(inscricao)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_nome_participante = QLabel(self.widget)
        self.lbl_nome_participante.setObjectName(u"lbl_nome_participante")

        self.verticalLayout.addWidget(self.lbl_nome_participante)

        self.txt_nome_participante = QLineEdit(self.widget)
        self.txt_nome_participante.setObjectName(u"txt_nome_participante")

        self.verticalLayout.addWidget(self.txt_nome_participante)

        self.lbl_email_participante = QLabel(self.widget)
        self.lbl_email_participante.setObjectName(u"lbl_email_participante")

        self.verticalLayout.addWidget(self.lbl_email_participante)

        self.txt_email_participante = QLineEdit(self.widget)
        self.txt_email_participante.setObjectName(u"txt_email_participante")

        self.verticalLayout.addWidget(self.txt_email_participante)

        self.cb_sessao = QComboBox(self.widget)
        self.cb_sessao.setObjectName(u"cb_sessao")
        self.cb_sessao.setEditable(True)

        self.verticalLayout.addWidget(self.cb_sessao)

        self.tb_sessao = QTableWidget(self.widget)
        if (self.tb_sessao.columnCount() < 2):
            self.tb_sessao.setColumnCount(2)
        font = QFont()
        font.setBold(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.tb_sessao.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.tb_sessao.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tb_sessao.setObjectName(u"tb_sessao")
        self.tb_sessao.horizontalHeader().setDefaultSectionSize(175)

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
        self.lbl_nome_participante.setText(QCoreApplication.translate("inscricao", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome do Participante</span></p></body></html>", None))
        self.lbl_email_participante.setText(QCoreApplication.translate("inscricao", u"<html><head/><body><p><span style=\" font-size:12pt;\">E-mail do Participante</span></p></body></html>", None))
        self.cb_sessao.setCurrentText(QCoreApplication.translate("inscricao", u"Selecione", None))
        ___qtablewidgetitem = self.tb_sessao.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("inscricao", u"Descri\u00e7\u00e3o Sess\u00e3o", None));
        ___qtablewidgetitem1 = self.tb_sessao.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("inscricao", u"Hor\u00e1rio Sess\u00e3o", None));
        self.btn_confirmar.setText(QCoreApplication.translate("inscricao", u"Confirmar", None))
    # retranslateUi

