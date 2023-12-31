# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'participante_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
from TrabalhoEventos.view import  resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(877, 686)
        icon = QIcon()
        icon.addFile(u":/icon/MicrosoftTeams-image.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_inicio = QWidget()
        self.tab_inicio.setObjectName(u"tab_inicio")
        self.verticalLayout_6 = QVBoxLayout(self.tab_inicio)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_6 = QWidget(self.tab_inicio)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setEnabled(True)
        self.widget_6.setMaximumSize(QSize(16777215, 200))
        self.widget_6.setStyleSheet(u"image: url(:/icon/MicrosoftTeams-image.png)")
        self.verticalLayout_5 = QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(10, 179, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.verticalLayout_6.addWidget(self.widget_6)

        self.btn_inscrever_participante = QPushButton(self.tab_inicio)
        self.btn_inscrever_participante.setObjectName(u"btn_inscrever_participante")

        self.verticalLayout_6.addWidget(self.btn_inscrever_participante)

        self.tb_lista_participante_inicio = QTableWidget(self.tab_inicio)
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
        self.tb_lista_participante_inicio.setEnabled(False)
        self.tb_lista_participante_inicio.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout_6.addWidget(self.tb_lista_participante_inicio)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.btn_atualizar_table = QPushButton(self.tab_inicio)
        self.btn_atualizar_table.setObjectName(u"btn_atualizar_table")
        self.btn_atualizar_table.setEnabled(True)

        self.horizontalLayout_7.addWidget(self.btn_atualizar_table)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab_inicio, "")
        self.tab_agenda = QWidget()
        self.tab_agenda.setObjectName(u"tab_agenda")
        self.verticalLayout_3 = QVBoxLayout(self.tab_agenda)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_email_participante = QLabel(self.tab_agenda)
        self.lbl_email_participante.setObjectName(u"lbl_email_participante")

        self.verticalLayout_3.addWidget(self.lbl_email_participante)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.txt_email_participante_agenda = QLineEdit(self.tab_agenda)
        self.txt_email_participante_agenda.setObjectName(u"txt_email_participante_agenda")

        self.horizontalLayout_5.addWidget(self.txt_email_participante_agenda)

        self.btn_consultar_email = QPushButton(self.tab_agenda)
        self.btn_consultar_email.setObjectName(u"btn_consultar_email")

        self.horizontalLayout_5.addWidget(self.btn_consultar_email)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.tb_lista_sessao_agenda = QTableWidget(self.tab_agenda)
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
        self.tb_lista_sessao_agenda.setEnabled(False)
        self.tb_lista_sessao_agenda.setAutoFillBackground(False)
        self.tb_lista_sessao_agenda.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout_3.addWidget(self.tb_lista_sessao_agenda)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tabWidget.addTab(self.tab_agenda, "")
        self.tab_participante = QWidget()
        self.tab_participante.setObjectName(u"tab_participante")
        self.verticalLayout_4 = QVBoxLayout(self.tab_participante)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_nome_participante = QLabel(self.tab_participante)
        self.lbl_nome_participante.setObjectName(u"lbl_nome_participante")

        self.verticalLayout_4.addWidget(self.lbl_nome_participante)

        self.txt_nome_participante = QLineEdit(self.tab_participante)
        self.txt_nome_participante.setObjectName(u"txt_nome_participante")

        self.verticalLayout_4.addWidget(self.txt_nome_participante)

        self.lbl_email_do_participante = QLabel(self.tab_participante)
        self.lbl_email_do_participante.setObjectName(u"lbl_email_do_participante")

        self.verticalLayout_4.addWidget(self.lbl_email_do_participante)

        self.txt_email_participante = QLineEdit(self.tab_participante)
        self.txt_email_participante.setObjectName(u"txt_email_participante")

        self.verticalLayout_4.addWidget(self.txt_email_participante)

        self.tb_participante = QTableWidget(self.tab_participante)
        if (self.tb_participante.columnCount() < 2):
            self.tb_participante.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_participante.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_participante.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        self.tb_participante.setObjectName(u"tb_participante")
        self.tb_participante.setEnabled(False)
        self.tb_participante.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout_4.addWidget(self.tb_participante)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btn_cadastrar = QPushButton(self.tab_participante)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")

        self.horizontalLayout_6.addWidget(self.btn_cadastrar)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.tabWidget.addTab(self.tab_participante, "")
        self.tab_criar_evento = QWidget()
        self.tab_criar_evento.setObjectName(u"tab_criar_evento")
        self.verticalLayout_2 = QVBoxLayout(self.tab_criar_evento)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_nome_evento = QLabel(self.tab_criar_evento)
        self.lbl_nome_evento.setObjectName(u"lbl_nome_evento")

        self.verticalLayout_2.addWidget(self.lbl_nome_evento)

        self.txt_nome_evento = QLineEdit(self.tab_criar_evento)
        self.txt_nome_evento.setObjectName(u"txt_nome_evento")

        self.verticalLayout_2.addWidget(self.txt_nome_evento)

        self.lbl_data_evento = QLabel(self.tab_criar_evento)
        self.lbl_data_evento.setObjectName(u"lbl_data_evento")

        self.verticalLayout_2.addWidget(self.lbl_data_evento)

        self.txt_data_evento = QLineEdit(self.tab_criar_evento)
        self.txt_data_evento.setObjectName(u"txt_data_evento")

        self.verticalLayout_2.addWidget(self.txt_data_evento)

        self.lbl_horario_evento = QLabel(self.tab_criar_evento)
        self.lbl_horario_evento.setObjectName(u"lbl_horario_evento")

        self.verticalLayout_2.addWidget(self.lbl_horario_evento)

        self.txt_horario_evento = QLineEdit(self.tab_criar_evento)
        self.txt_horario_evento.setObjectName(u"txt_horario_evento")

        self.verticalLayout_2.addWidget(self.txt_horario_evento)

        self.tableWidget = QTableWidget(self.tab_criar_evento)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_criar_evento = QPushButton(self.tab_criar_evento)
        self.btn_criar_evento.setObjectName(u"btn_criar_evento")

        self.horizontalLayout_4.addWidget(self.btn_criar_evento)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.tabWidget.addTab(self.tab_criar_evento, "")
        self.tab_criar_sessao = QWidget()
        self.tab_criar_sessao.setObjectName(u"tab_criar_sessao")
        self.verticalLayout = QVBoxLayout(self.tab_criar_sessao)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_tema_sessao = QLabel(self.tab_criar_sessao)
        self.lbl_tema_sessao.setObjectName(u"lbl_tema_sessao")

        self.verticalLayout.addWidget(self.lbl_tema_sessao)

        self.txt_tema_sessao = QLineEdit(self.tab_criar_sessao)
        self.txt_tema_sessao.setObjectName(u"txt_tema_sessao")

        self.verticalLayout.addWidget(self.txt_tema_sessao)

        self.lbl_palestrante_sessao = QLabel(self.tab_criar_sessao)
        self.lbl_palestrante_sessao.setObjectName(u"lbl_palestrante_sessao")

        self.verticalLayout.addWidget(self.lbl_palestrante_sessao)

        self.txt_palestrante_sessao = QLineEdit(self.tab_criar_sessao)
        self.txt_palestrante_sessao.setObjectName(u"txt_palestrante_sessao")

        self.verticalLayout.addWidget(self.txt_palestrante_sessao)

        self.lbl_horario_sessao = QLabel(self.tab_criar_sessao)
        self.lbl_horario_sessao.setObjectName(u"lbl_horario_sessao")

        self.verticalLayout.addWidget(self.lbl_horario_sessao)

        self.txt_horario_sessao = QLineEdit(self.tab_criar_sessao)
        self.txt_horario_sessao.setObjectName(u"txt_horario_sessao")

        self.verticalLayout.addWidget(self.txt_horario_sessao)

        self.cb_tipo_evento_sessao = QComboBox(self.tab_criar_sessao)
        self.cb_tipo_evento_sessao.addItem("")
        self.cb_tipo_evento_sessao.setObjectName(u"cb_tipo_evento_sessao")
        self.cb_tipo_evento_sessao.setEditable(False)

        self.verticalLayout.addWidget(self.cb_tipo_evento_sessao)

        self.tb_lista_sessao_criar_sessao = QTableWidget(self.tab_criar_sessao)
        if (self.tb_lista_sessao_criar_sessao.columnCount() < 4):
            self.tb_lista_sessao_criar_sessao.setColumnCount(4)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_lista_sessao_criar_sessao.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_lista_sessao_criar_sessao.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_lista_sessao_criar_sessao.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_lista_sessao_criar_sessao.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        self.tb_lista_sessao_criar_sessao.setObjectName(u"tb_lista_sessao_criar_sessao")
        self.tb_lista_sessao_criar_sessao.setEnabled(False)
        self.tb_lista_sessao_criar_sessao.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout.addWidget(self.tb_lista_sessao_criar_sessao)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_criar_sessao = QPushButton(self.tab_criar_sessao)
        self.btn_criar_sessao.setObjectName(u"btn_criar_sessao")

        self.horizontalLayout_2.addWidget(self.btn_criar_sessao)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tabWidget.addTab(self.tab_criar_sessao, "")

        self.horizontalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_inscrever_participante.setText(QCoreApplication.translate("MainWindow", u"Inscrever e Desinscrever Participante", None))
        ___qtablewidgetitem = self.tb_lista_participante_inicio.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome do Participante", None));
        ___qtablewidgetitem1 = self.tb_lista_participante_inicio.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Email do Participante", None));
        ___qtablewidgetitem2 = self.tb_lista_participante_inicio.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Evento", None));
        ___qtablewidgetitem3 = self.tb_lista_participante_inicio.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Sess\u00e3o", None));
        self.btn_atualizar_table.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_inicio), QCoreApplication.translate("MainWindow", u"In\u00edcio", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_agenda), QCoreApplication.translate("MainWindow", u"Agenda", None))
        self.lbl_nome_participante.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome do Participante</span></p></body></html>", None))
        self.lbl_email_do_participante.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">E-mail do Participante</span></p></body></html>", None))
        ___qtablewidgetitem8 = self.tb_participante.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nome do Participante", None));
        ___qtablewidgetitem9 = self.tb_participante.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"E-mail do Participante", None));
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_participante), QCoreApplication.translate("MainWindow", u"Participante", None))
        self.lbl_nome_evento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Nome do Evento</span></p></body></html>", None))
        self.lbl_data_evento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Data do Evento</span></p></body></html>", None))
        self.txt_data_evento.setInputMask(QCoreApplication.translate("MainWindow", u"99/99/9999", None))
        self.txt_data_evento.setText(QCoreApplication.translate("MainWindow", u"//", None))
        self.lbl_horario_evento.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hor\u00e1rio do Evento</span></p></body></html>", None))
        self.txt_horario_evento.setInputMask(QCoreApplication.translate("MainWindow", u"99:99", None))
        self.txt_horario_evento.setText(QCoreApplication.translate("MainWindow", u":", None))
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nome do Evento", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Data do Evento", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio do Evento", None));
        self.btn_criar_evento.setText(QCoreApplication.translate("MainWindow", u"Criar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_criar_evento), QCoreApplication.translate("MainWindow", u"Criar Evento", None))
        self.lbl_tema_sessao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Tema da Sess\u00e3o</span></p></body></html>", None))
        self.lbl_palestrante_sessao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Palestrante da Sess\u00e3o</span></p></body></html>", None))
        self.lbl_horario_sessao.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">Hor\u00e1rio da Sess\u00e3o</span></p></body></html>", None))
        self.txt_horario_sessao.setInputMask(QCoreApplication.translate("MainWindow", u"99:99", None))
        self.txt_horario_sessao.setText(QCoreApplication.translate("MainWindow", u":", None))
        self.cb_tipo_evento_sessao.setItemText(0, QCoreApplication.translate("MainWindow", u"Selecione o Evento", None))

        self.cb_tipo_evento_sessao.setCurrentText(QCoreApplication.translate("MainWindow", u"Selecione o Evento", None))
        ___qtablewidgetitem13 = self.tb_lista_sessao_criar_sessao.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tema da Sess\u00e3o", None));
        ___qtablewidgetitem14 = self.tb_lista_sessao_criar_sessao.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Palestrante da Sess\u00e3o", None));
        ___qtablewidgetitem15 = self.tb_lista_sessao_criar_sessao.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio da Sess\u00e3o", None));
        ___qtablewidgetitem16 = self.tb_lista_sessao_criar_sessao.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Evento", None));
        self.btn_criar_sessao.setText(QCoreApplication.translate("MainWindow", u"Criar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_criar_sessao), QCoreApplication.translate("MainWindow", u"Criar Sess\u00e3o", None))
    # retranslateUi

