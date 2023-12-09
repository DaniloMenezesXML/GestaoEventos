from datetime import datetime
from PySide6.QtWidgets import QMessageBox

from TrabalhoEventos.infra.entities.inscricao import Inscricao
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


    def insert_inscricao(self, inscricao_ui):
        if inscricao_ui.cb_evento.currentText() != 'Selecione o Evento':
            participante = self.evento_repository.select_evento_by_nome(inscricao_ui.cb_evento.currentText())
            inscricao_ui.select_evento = None
            if inscricao_ui.cb_sessao.currentText() != 'Selecione a Sessão':
                participante2 = self.sessao_repository.select_sessao_by_tema(inscricao_ui.cb_sessao.currentText())
                inscricao_ui.select_sessao = None
                inscricao = Inscricao()
                inscricao.tema = inscricao_ui.txt_tema_sessao.text()
                inscricao.palestrante = inscricao_ui.txt_palestrante_sessao.text()
                inscricao.horario_sessao = inscricao_ui.txt_horario_sessao.text()
                hora = inscricao.horario_sessao
                hora = datetime.strptime(hora, '%H:%M').time()
                inscricao.horario_sessao = hora
                try:
                    self.inscricao_repository.insert_sessao(inscricao)
                    inscricao_ui.txt_tema_sessao.setText('')
                    inscricao_ui.txt_palestrante_sessao.setText('')
                    inscricao_ui.txt_horario_sessao.setText('')

                    self.inscricao_repository.insert_sessao(inscricao_ui.select_evento, inscricao_ui.select_sessao, participante, participante2, inscricao_ui)
                    QMessageBox.information(inscricao_ui, 'Inscrição', 'Inscrição criada com sucesso!')
                except Exception as e:
                    QMessageBox.warning(inscricao_ui, 'Inscrição', f'Erro ao cadastrar inscrição! \nErro: {e}')



