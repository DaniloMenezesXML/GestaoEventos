from PySide6.QtWidgets import QMessageBox

from TrabalhoEventos.infra.entities.participante import Participante
from TrabalhoEventos.infra.repository.sessao_repository import SessaoRepository
from TrabalhoEventos.infra.repository.participante_repository import ParticipanteRepository
from TrabalhoEventos.infra.repository.evento_repository import EventoRepository
from TrabalhoEventos.services.main_window_service import MainWindowService


class ParticipanteService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.sessao_repository = SessaoRepository()
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()

    def insert_Participante(self, inscricao_ui):
        participante = Participante()
        participante.nome = inscricao_ui.txt_nome_participante.text()
        participante.email = inscricao_ui.txt_email_participante.text()
        participante.ativo = True
        try:
            self.participante_repository.insert_one_funcionario(participante)
            inscricao_ui.txt_nome_participante.setText('')
            inscricao_ui.txt_email_participante.setText('')
            self.service_main_window.populate_table_participante(inscricao_ui)
            QMessageBox.information(inscricao_ui, 'Participantes', f'Participante cadastrado com sucesso.')
        except Exception as e:
            QMessageBox.information(inscricao_ui, 'Participantes', f'Erro ao cadastrar Participante!\n Erro{e}')



    def select_participante(self, participante_ui):
        if participante_ui.btn_consultar_email.text() == 'Consultar':
            participante_ui.txt_email_participante_agenda.setText('')
            participante_ui.txt_email_participante_agenda.setReadOnly(False)
            participante_ui.selected_participante = None
            participante_ui.btn_consultar_email.setText('Consultar')
        else:
            try:
                if participante_ui.txt_email_participante_agenda.text() != '':
                    participante_inscrito = (self.participante_repository.select_participante_by_email
                                              (participante_ui.txt_email_participante_agenda.text()))
                    participante_ui.selected_participante = participante_inscrito
                    participante_ui.txt_email_participante_agenda.setReadOnly(True)
                    participante_ui.btn_consultar_email.setText('Limpar')

                else:
                    QMessageBox.information(participante_ui, 'Participante', f'Insira um E-mail para consultar Participante!\n Erro{e}')
            except Exception as e:
                QMessageBox.information(participante_ui, 'Participante', f'Erro ao consultar Participante!\n Erro{e}')


    def delete_participante(self, inscricao_ui, participante_ui):
        selected_rows = (participante_ui.tb_lista_participante_inicio.selectionModel().selectedRows(),
                         participante_ui.tb_lista_sessao_agenda.selectionModel().selectedRows())
        if not selected_rows:
            return
        selected_row = selected_rows[0].row()
        participante_delete = self.participante_repository.select_participante_by_email(
            participante_ui.tb_lista_participante_inicio.item(selected_row, 1).text(),
            participante_ui.tb_lista_sessao_agenda.item(selected_row, 1).text()
        )
        msg_box = QMessageBox(participante_ui)
        msg_box.setWindowTitle('Desinscrever Participante')
        msg_box.setText(f'Tem certeza que deseja desinscrever o participante {participante_delete.nome}')
        msg_box.setIcon(QMessageBox.Question)
        yes_button = msg_box.addButton('Sim', QMessageBox.YesRole)
        no_button = msg_box.addButton('Não', QMessageBox.NoRole)
        msg_box.exec()
        if msg_box.clickedButton() == yes_button:
            try:
                self.participante_repository.delete_participante(participante_delete)
                self.service_main_window.populate_table_participante(participante_ui)
            except Exception as e:
                QMessageBox.warning(participante_ui, f'Atenção, Problema ao desinscrever participante. \n Erro{e}')

