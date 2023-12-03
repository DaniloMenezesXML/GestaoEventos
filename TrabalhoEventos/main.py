import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QPalette, QColor, Qt

from TrabalhoEventos.services.main_window_service import MainWindowService
from TrabalhoEventos.view.participante_ui import Ui_MainWindow
from TrabalhoEventos.view.inscricao_ui import Ui_inscricao
from TrabalhoEventos.infra.config.connection import DBConnectionHandler
from TrabalhoEventos.services.evento_service import EventoService
from TrabalhoEventos.services.participante_service import ParticipanteService
from TrabalhoEventos.services.sessao_service import SessaoService

class Mainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Mainwindow, self).__init__()
        self.setupUi(self)
        self.btn_inscrever_participante.clicked.connect(self.inscricao_participante)
        data_base = DBConnectionHandler()

        self.main_window_service = MainWindowService()
        self.uniforme_to_update = None
        self.sessao_service = SessaoService()
        self.evento_service = EventoService()
        self.participante_service = ParticipanteService()
        self.main_window_service.populate_table_evento(self)
        self.main_window_service.populate_table_sessao(self)
        self.main_window_service.populate_table_lista_participante(self)

        self.btn_inscrever_participante.clicked.connect(self.inscricao_participante)
        self.btn_desinscrever_participante.clicked.connect(self.desinscrever_participante)

        self.btn_criar_sessao.clicked.connect(self.criar_sessao)

        self.btn_criar_evento.clicked.connect(self.criar_evento)

        self.btn_consultar_email.clicked.connect(self.consultar_email)

    def criar_evento(self):
        self.evento_service.insert_evento(self)

    def criar_sessao(self):
        self.sessao_service.insert_sessao(self)

    def desinscrever_participante(self):
        self.participante_service.delete_participante(self)

    def consultar_email(self):
        self.participante_service.select_participante_by_email(self)

    def inscricao_participante(self):
        self.inscricao_dialog = InscricaoDialog(self)
        self.inscricao_dialog.finished.connect(self.on_inscricao_closed)
        self.inscricao_dialog.show()
        self.hide()
        self.inscricao_dialog.finished.connect(
            lambda: self.main_window_service.populate_table_lista_participante(self))


    def on_inscricao_closed(self):
        self.show()

class InscricaoDialog(QDialog, Ui_inscricao):
    def __init__(self, parent=None):
        super(InscricaoDialog, self).__init__(parent)
        self.setupUi(self)
        self.selected_participante = None
        self.eventoz = []
        self.main_window_service = MainWindowService()
        self.sessao_service = SessaoService()
        self.evento_service = EventoService()
        self.parcipante_service = ParticipanteService()
        self.main_window_service.populate_sessoes_combo(self)

        self.btn_consultar_email.clicked.connect(self.get_participante)

    def get_funcionario(self):
        self.parcipante_service.select_participante_by_email(self)

if __name__ == "__main__":
    app = QApplication()

    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
    palette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.black)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, QColor(127, 127, 127))
    app.setPalette(palette)
    app.setStyle('Fusion')
    window = Mainwindow()
    window.show()
    sys.exit(app.exec())
