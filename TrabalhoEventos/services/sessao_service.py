from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from TrabalhoEventos.infra.entities.sessao import Sessao
from TrabalhoEventos.infra.repository.evento_repository import EventoRepository
from TrabalhoEventos.infra.repository.inscricao_repository import InscricaoRepository
from TrabalhoEventos.infra.repository.participante_repository import ParticipanteRepository
from TrabalhoEventos.infra.repository.sessao_repository import SessaoRepository
from TrabalhoEventos.services.main_window_service import MainWindowService


class SessaoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()
        self.sessao_repository = SessaoRepository()
        self.inscricao_repository = InscricaoRepository()

    def insert_sessao(self, main_window):
        sessao = Sessao()
        sessao.nome = main_window.txt_tema_sessao.text()
        sessao.data_evento = main_window.txt_data_evento.text()
        sessao.horario_sessao = main_window.txt_horario_evento.text()

        try:
            self.evento_repository.insert_one_evento(sessao)
            main_window.txt_tema_sessao.setText('')
            main_window.txt_palestrante_sessao.setText('')
            main_window.txt_horario_sessao.setText('')

            self.service_main_window.populate_table_sessao(main_window)
            QMessageBox.information(main_window, 'Sessao', 'Sessao cadastrado com sucesso!')
        except Exception as e:
            QMessageBox.warning(main_window, 'Sessao', f'Erro ao cadastrar sessao! \nErro: {e}')






