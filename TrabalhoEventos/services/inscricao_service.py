from datetime import datetime
from PySide6.QtWidgets import QMessageBox

from TrabalhoEventos.infra.entities.inscricao import Inscricao
from TrabalhoEventos.infra.entities.sessao import Sessao
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
                sessao = Sessao()
                inscricao.tema = inscricao_ui.cb_sessao.currentText()
                sessao.palestrante = inscricao_ui.txt_palestrante_sessao.text()
                sessao.horario_sessao = inscricao_ui.txt_horario_sessao.text()
                inscricao.palestrante = sessao.palestrante
                inscricao.horario_sessao = sessao.horario_sessao
                inscricao.nome_evento = inscricao_ui.cb_evento.currentText()
                hora = inscricao.horario_sessao
                hora = datetime.strptime(hora, '%H:%M').time()
                inscricao.horario_sessao = hora
                try:
                    self.inscricao_repository.insert_inscricao(inscricao)
                    inscricao_ui.txt_tema_sessao.setText('')
                    inscricao_ui.txt_palestrante_sessao.setText('')
                    inscricao_ui.txt_horario_sessao.setText('')

                    self.inscricao_repository.insert_inscricao(inscricao_ui.select_evento, inscricao_ui.select_sessao, participante, participante2, inscricao_ui)
                    QMessageBox.information(inscricao_ui, 'Inscrição', 'Inscrição criada com sucesso!')
                except Exception as e:
                    QMessageBox.warning(inscricao_ui, 'Inscrição', f'Erro ao cadastrar inscrição! \nErro: {e}')

    def select_participante_inscricao(self, inscricao_ui):
        if inscricao_ui.btn_consultar.text() == 'Limpar':
            inscricao_ui.txt_nome_participante.setText('')
            inscricao_ui.txt_email_participante.setText('')
            inscricao_ui.txt_email_participante.setReadOnly(False)
            inscricao_ui.selected_participante = None
            inscricao_ui.pushButton.setText('Consultar')
        else:
            try:
                if inscricao_ui.txt_email_participante.text() != '':
                    inscricao_participante = (self.participante_repository.select_participante_by_email
                                              (inscricao_ui.txt_email_participante.text()))
                    inscricao_ui.selected_funcionario = inscricao_participante
                    inscricao_ui.txt_nome_participante.setText(inscricao_participante.nome)
                    inscricao_ui.txt_email_participante.setReadOnly(True)
                    inscricao_ui.btn_consultar.setText('Limpar')

                else:
                    QMessageBox.information(inscricao_ui, 'Participantes',
                                            f'Insira um e-mail para consultar o participante!\n Erro')
            except Exception as e:
                QMessageBox.information(inscricao_ui, 'Participantes', f'Erro ao consultar participante!\n Erro{e}')

                inscricao_ui.txt_nome_participante.clear()


