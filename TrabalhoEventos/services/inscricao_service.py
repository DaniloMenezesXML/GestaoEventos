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
            if inscricao_ui.cb_sessao.currentText() != 'Selecione a Sessão':
                inscricao = Inscricao()
                inscricao.email_participante = inscricao_ui.txt_email_participante.text()
                inscricao.tema = inscricao_ui.cb_sessao.currentText()
                inscricao.nome_evento = inscricao_ui.cb_evento.currentText()
                print(
                    f"Inserting Inscricao - Inscricao: {inscricao.tema}, Email: {inscricao.email_participante}, Palestrante: {inscricao.palestrante}, Evento Nome: {inscricao.nome_evento} Evento Nome: {inscricao.horario_sessao}")
                try:
                    evento_id = self.evento_repository.select_evento_by_nome_return_id(inscricao.nome_evento)
                    participante_id = self.participante_repository.select_participante_by_email_return_id(inscricao.email_participante)
                    sessao_id = self.sessao_repository.select_sessao_by_tema_return_id(inscricao.tema)
                    print(
                        f"Inserting Iscricao - Participante: {participante_id}, Evento: {evento_id}, Sessao: {sessao_id}")
                    print(
                        f"Inserting Inscricao - Inscricao: {inscricao.tema}, Email: {inscricao.email_participante}, Palestrante: {inscricao.palestrante}, Evento Nome: {inscricao.nome_evento} Horario Sessao: {inscricao.horario_sessao}")

                    if evento_id is not None and participante_id is not None and sessao_id is not None:
                        self.inscricao_repository.insert_inscricao(inscricao.sessao_id, inscricao.evento_id, inscricao.participante_id, inscricao)
                        inscricao_ui.txt_email_participante.setText('')
                        inscricao_ui.txt_nome_participante.setText('')
                        self.service_main_window.populate_table_sessao(inscricao_ui)
                        QMessageBox.information(inscricao_ui, 'Inscricao', 'Participante inscrito com sucesso!')
                    else:
                        QMessageBox.warning(inscricao_ui, 'Inscricao', 'Participante não encontrado!')
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


