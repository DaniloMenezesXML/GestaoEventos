from datetime import datetime
from PySide6.QtWidgets import QMessageBox

from TrabalhoEventos.infra.entities.insricao import Inscricao
from TrabalhoEventos.infra.repository.sessao_repository import SessaoRepository
from TrabalhoEventos.infra.repository.inscricao_repository import InscricaoRepository
from TrabalhoEventos.infra.repository.evento_repository import EventoRepository
from TrabalhoEventos.infra.repository.participante_repository import ParticipanteRepository
from TrabalhoEventos.services.main_window_service import MainWindowService

class InscricaoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()
        self.sessao_repository = SessaoRepository()
        self.inscricao_repository = InscricaoRepository()


    def insert_inscricao(self, participante_ui):
        if participante_ui.cb_tipo_evento_sessao.currentText() != 'Selecione o evento' and participante_ui.txt_tema_sessao is not None:
            participante = self.evento_repository.select_evento_by_nome(participante_ui.cb_tipo_evento_sessao.currentText())
            participante_ui.select_evento = None
            inscricao = Inscricao()
            inscricao.tema = participante_ui.txt_tema_sessao.text()
            inscricao.palestrante = participante_ui.txt_palestrante_sessao.text()
            inscricao.horario_sessao = participante_ui.txt_horario_sessao.text()
            hora = inscricao.horario_sessao
            hora = datetime.strptime(hora, '%H:%M').time()
            inscricao.horario_sessao = hora
            try:
                self.sessao_repository.insert_sessao(inscricao)
                participante_ui.txt_tema_sessao.setText('')
                participante_ui.txt_palestrante_sessao.setText('')
                participante_ui.txt_horario_sessao.setText('')

                self.sessao_repository.insert_sessao(participante_ui.select_evento, participante, participante_ui)
                QMessageBox.information(participante_ui, 'Inscrição', 'Inscrição criada com sucesso!')
            except Exception as e:
                QMessageBox.warning(participante_ui, 'Inscrição', f'Erro ao cadastrar inscrição! \nErro: {e}')



