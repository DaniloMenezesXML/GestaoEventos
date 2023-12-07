from datetime import datetime
from PySide6.QtWidgets import QMessageBox

from TrabalhoEventos.infra.entities.sessao import Sessao
from TrabalhoEventos.infra.repository.sessao_repository import SessaoRepository
from TrabalhoEventos.infra.repository.evento_repository import EventoRepository
from TrabalhoEventos.infra.repository.participante_repository import ParticipanteRepository
from TrabalhoEventos.services.main_window_service import MainWindowService

class SessaoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()
        self.sessao_repository = SessaoRepository()


    def insert_sessao(self, participante_ui):
        if participante_ui.cb_tipo_evento_sessao.currentText() != 'Selecione o evento' and participante_ui.txt_tema_sessao is not None:
            participante = self.evento_repository.select_evento_by_nome(participante_ui.cb_tipo_evento_sessao.currentText())
            participante_ui.select_evento = None
            sessao = Sessao()
            sessao.tema = participante_ui.txt_tema_sessao.text()
            sessao.palestrante = participante_ui.txt_palestrante_sessao.text()
            sessao.horario_sessao = participante_ui.txt_horario_sessao.text()
            hora = sessao.horario_sessao
            hora = datetime.strptime(hora, '%H:%M').time()
            sessao.horario_sessao = hora
            try:
                self.sessao_repository.insert_sessao(sessao)
                participante_ui.txt_tema_sessao.setText('')
                participante_ui.txt_palestrante_sessao.setText('')
                participante_ui.txt_horario_sessao.setText('')

                self.sessao_repository.insert_sessao(participante_ui.select_evento, participante, participante_ui)
                QMessageBox.information(participante_ui, 'Sessoes', 'Sessao criada com sucesso!')
            except Exception as e:
                QMessageBox.warning(participante_ui, 'Sessoes', f'Erro ao cadastrar sessão! \nErro: {e}')



