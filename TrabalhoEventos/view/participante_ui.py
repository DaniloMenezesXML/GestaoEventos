# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'participante_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import icon 1_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(891, 745)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.inicio = QWidget()
        self.inicio.setObjectName(u"inicio")
        self.verticalLayout_15 = QVBoxLayout(self.inicio)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_6 = QWidget(self.inicio)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setEnabled(True)
        self.widget_6.setMaximumSize(QSize(16777215, 200))
        self.widget_6.setStyleSheet(u"image: url(:/icon/MicrosoftTeams-image.png)")
        self.verticalLayout_14 = QVBoxLayout(self.widget_6)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalSpacer_2 = QSpacerItem(10, 254, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)


        self.verticalLayout_15.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.inicio)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.btn_inscrever_participante = QPushButton(self.widget_5)
        self.btn_inscrever_participante.setObjectName(u"btn_inscrever_participante")

        self.verticalLayout_6.addWidget(self.btn_inscrever_participante)

        self.btn_desinscrever_participante = QPushButton(self.widget_5)
        self.btn_desinscrever_participante.setObjectName(u"btn_desinscrever_participante")

        self.verticalLayout_6.addWidget(self.btn_desinscrever_participante)

        self.cb_filtrar_evento = QComboBox(self.widget_5)
        self.cb_filtrar_evento.setObjectName(u"cb_filtrar_evento")
        self.cb_filtrar_evento.setEditable(True)

        self.verticalLayout_6.addWidget(self.cb_filtrar_evento)

        self.tb_lista_participante_inicio = QTableWidget(self.widget_5)
        if (self.tb_lista_participante_inicio.columnCount() < 4):
            self.tb_lista_participante_inicio.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_lista_participante_inicio.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_lista_participante_inicio.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_lista_participante_inicio.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_lista_participante_inicio.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_lista_participante_inicio.setObjectName(u"tb_lista_participante_inicio")
        self.tb_lista_participante_inicio.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout_6.addWidget(self.tb_lista_participante_inicio)


        self.verticalLayout_15.addWidget(self.widget_5)

        self.tabWidget.addTab(self.inicio, "")
        self.agenda = QWidget()
        self.agenda.setObjectName(u"agenda")
        self.verticalLayout_12 = QVBoxLayout(self.agenda)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_4 = QWidget(self.agenda)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_11 = QVBoxLayout(self.widget_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lbl_email_participante = QLabel(self.widget_4)
        self.lbl_email_participante.setObjectName(u"lbl_email_participante")

        self.verticalLayout_11.addWidget(self.lbl_email_participante)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_email_participante_agenda = QLineEdit(self.widget_4)
        self.txt_email_participante_agenda.setObjectName(u"txt_email_participante_agenda")

        self.horizontalLayout_5.addWidget(self.txt_email_participante_agenda)

        self.btn_consultar_email = QPushButton(self.widget_4)
        self.btn_consultar_email.setObjectName(u"btn_consultar_email")

        self.horizontalLayout_5.addWidget(self.btn_consultar_email)


        self.verticalLayout_11.addLayout(self.horizontalLayout_5)

        self.tb_lista_sessao_agenda = QTableWidget(self.widget_4)
        if (self.tb_lista_sessao_agenda.columnCount() < 4):
            self.tb_lista_sessao_agenda.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_lista_sessao_agenda.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_lista_sessao_agenda.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_lista_sessao_agenda.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_lista_sessao_agenda.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.tb_lista_sessao_agenda.setObjectName(u"tb_lista_sessao_agenda")
        self.tb_lista_sessao_agenda.setEnabled(True)
        self.tb_lista_sessao_agenda.setAutoFillBackground(False)
        self.tb_lista_sessao_agenda.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout_11.addWidget(self.tb_lista_sessao_agenda)


        self.verticalLayout_12.addWidget(self.widget_4)

        self.tabWidget.addTab(self.agenda, "")
        self.criar_evento = QWidget()
        self.criar_evento.setObjectName(u"criar_evento")
        self.verticalLayout_3 = QVBoxLayout(self.criar_evento)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.criar_evento)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_nome_evento = QLabel(self.widget_2)
        self.lbl_nome_evento.setObjectName(u"lbl_nome_evento")

        self.verticalLayout_4.addWidget(self.lbl_nome_evento)

        self.txt_nome_evento = QLineEdit(self.widget_2)
        self.txt_nome_evento.setObjectName(u"txt_nome_evento")

        self.verticalLayout_4.addWidget(self.txt_nome_evento)

        self.lbl_data_evento = QLabel(self.widget_2)
        self.lbl_data_evento.setObjectName(u"lbl_data_evento")

        self.verticalLayout_4.addWidget(self.lbl_data_evento)

        self.txt_data_evento = QLineEdit(self.widget_2)
        self.txt_data_evento.setObjectName(u"txt_data_evento")

        self.verticalLayout_4.addWidget(self.txt_data_evento)

        self.lbl_horario_evento = QLabel(self.widget_2)
        self.lbl_horario_evento.setObjectName(u"lbl_horario_evento")

        self.verticalLayout_4.addWidget(self.lbl_horario_evento)

        self.txt_horario_evento = QLineEdit(self.widget_2)
        self.txt_horario_evento.setObjectName(u"txt_horario_evento")

        self.verticalLayout_4.addWidget(self.txt_horario_evento)

        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(548, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.btn_criar_evento = QPushButton(self.widget_2)
        self.btn_criar_evento.setObjectName(u"btn_criar_evento")

        self.horizontalLayout_3.addWidget(self.btn_criar_evento)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.tabWidget.addTab(self.criar_evento, "")
        self.criar_sessao = QWidget()
        self.criar_sessao.setObjectName(u"criar_sessao")
        self.verticalLayout_10 = QVBoxLayout(self.criar_sessao)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_3 = QWidget(self.criar_sessao)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_tema_sessao = QLabel(self.widget_3)
        self.lbl_tema_sessao.setObjectName(u"lbl_tema_sessao")

        self.verticalLayout.addWidget(self.lbl_tema_sessao)

        self.txt_tema_sessao = QLineEdit(self.widget_3)
        self.txt_tema_sessao.setObjectName(u"txt_tema_sessao")

        self.verticalLayout.addWidget(self.txt_tema_sessao)

        self.lbl_palestrante_sessao = QLabel(self.widget_3)
        self.lbl_palestrante_sessao.setObjectName(u"lbl_palestrante_sessao")

        self.verticalLayout.addWidget(self.lbl_palestrante_sessao)

        self.txt_palestrante_sessao = QLineEdit(self.widget_3)
        self.txt_palestrante_sessao.setObjectName(u"txt_palestrante_sessao")

        self.verticalLayout.addWidget(self.txt_palestrante_sessao)

        self.lbl_horario_sessao = QLabel(self.widget_3)
        self.lbl_horario_sessao.setObjectName(u"lbl_horario_sessao")

        self.verticalLayout.addWidget(self.lbl_horario_sessao)

        self.txt_horario_sessao = QLineEdit(self.widget_3)
        self.txt_horario_sessao.setObjectName(u"txt_horario_sessao")

        self.verticalLayout.addWidget(self.txt_horario_sessao)

        self.cb_tipo_evento_sessao = QComboBox(self.widget_3)
        self.cb_tipo_evento_sessao.setObjectName(u"cb_tipo_evento_sessao")
        self.cb_tipo_evento_sessao.setEditable(True)

        self.verticalLayout.addWidget(self.cb_tipo_evento_sessao)

        self.tb_lista_sessao_criar_sessao = QTableWidget(self.widget_3)
        if (self.tb_lista_sessao_criar_sessao.columnCount() < 3):
            self.tb_lista_sessao_criar_sessao.setColumnCount(3)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_lista_sessao_criar_sessao.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_lista_sessao_criar_sessao.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_lista_sessao_criar_sessao.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        self.tb_lista_sessao_criar_sessao.setObjectName(u"tb_lista_sessao_criar_sessao")
        self.tb_lista_sessao_criar_sessao.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout.addWidget(self.tb_lista_sessao_criar_sessao)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(548, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_criar_sessao = QPushButton(self.widget_3)
        self.btn_criar_sessao.setObjectName(u"btn_criar_sessao")

        self.horizontalLayout_4.addWidget(self.btn_criar_sessao)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_10.addWidget(self.widget_3)

        self.tabWidget.addTab(self.criar_sessao, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_5.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_inscrever_participante.setText(QCoreApplication.translate("MainWindow", u"Inscrever Participante", None))
        self.btn_desinscrever_participante.setText(QCoreApplication.translate("MainWindow", u"Desinscrever Participante", None))
        self.cb_filtrar_evento.setCurrentText(QCoreApplication.translate("MainWindow", u"Filtrar por Evento", None))
        ___qtablewidgetitem = self.tb_lista_participante_inicio.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome do Participante", None));
        ___qtablewidgetitem1 = self.tb_lista_participante_inicio.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Email do Participante", None));
        ___qtablewidgetitem2 = self.tb_lista_participante_inicio.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Evento", None));
        ___qtablewidgetitem3 = self.tb_lista_participante_inicio.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sess\u00e3o", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inicio), QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
        self.lbl_email_participante.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">E-mail do Participante</span></p></body></html>", None))
        self.btn_consultar_email.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        ___qtablewidgetitem4 = self.tb_lista_sessao_agenda.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nome do Participante", None));
        ___qtablewidgetitem5 = self.tb_lista_sessao_agenda.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Evento", None));
        ___qtablewidgetitem6 = self.tb_lista_sessao_agenda.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Sess\u00e3o", None));
        ___qtablewidgetitem7 = self.tb_lista_sessao_agenda.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio da Sessao", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.agenda), QCoreApplication.translate("MainWindow", u"Agenda", None))
        self.lbl_nome_evento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome do Evento</span></p></body></html>", None))
        self.lbl_data_evento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Data do Evento</span></p></body></html>", None))
        self.lbl_horario_evento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hor\u00e1rio do Evento</span></p></body></html>", None))
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nome do Evento", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data do Evento", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio do Evento", None));
        self.btn_criar_evento.setText(QCoreApplication.translate("MainWindow", u"Criar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.criar_evento), QCoreApplication.translate("MainWindow", u"Criar Evento", None))
        self.lbl_tema_sessao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tema da Sess\u00e3o</span></p></body></html>", None))
        self.lbl_palestrante_sessao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Palestrante da Sess\u00e3o</span></p></body></html>", None))
        self.lbl_horario_sessao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hor\u00e1rio da Sess\u00e3o</span></p></body></html>", None))
        self.cb_tipo_evento_sessao.setCurrentText(QCoreApplication.translate("MainWindow", u"Selecione o Evento", None))
        ___qtablewidgetitem11 = self.tb_lista_sessao_criar_sessao.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Tema da Sess\u00e3o", None));
        ___qtablewidgetitem12 = self.tb_lista_sessao_criar_sessao.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Palestrante da Sess\u00e3o", None));
        ___qtablewidgetitem13 = self.tb_lista_sessao_criar_sessao.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio da Sess\u00e3o", None));
        self.btn_criar_sessao.setText(QCoreApplication.translate("MainWindow", u"Criar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.criar_sessao), QCoreApplication.translate("MainWindow", u"Criar Sess\u00e3o", None))
    # retranslateUi
