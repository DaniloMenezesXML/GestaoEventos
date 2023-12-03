from PySide6.QtWidgets import QMessageBox

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
        texto = participante_ui.cb_tipo_evento_sessao.currentText()
        if participante_ui.cb_tipo_evento_sessao.currentText() != 'Selecione o evento' and participante_ui.txt_tema_sessao is not None:
            participante = self.sessao_repository.select_Evento_by_name(participante_ui.cb_tipo_evento_sessao.currentText())
            try:
                self.sessao_repository.insert_sessao(participante_ui.select_evento)
                QMessageBox.information(participante_ui, 'Sessoes', 'Sessao criada com sucesso!')
            except Exception as e:
                QMessageBox.warning(participante_ui, 'Sessoes', f'Erro ao cadastrar sessão! \nErro: {e}')



