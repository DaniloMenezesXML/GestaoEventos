from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from TrabalhoEventos.infra.entities.sessao import Sessao
from TrabalhoEventos.infra.repository.evento_repository import EventoRepository
from TrabalhoEventos.infra.repository.participante_repository import ParticipanteRepository
from TrabalhoEventos.infra.repository.sessao_repository import SessaoRepository
from TrabalhoEventos.services.main_window_service import MainWindowService


class SessaoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()
        self.sessao_repository = SessaoRepository()

    def insert_sessao(self, participante_ui):
        sessao = Sessao()
        sessao.tema = participante_ui.txt_tema_sessao.text()
        sessao.palestrante = participante_ui.txt_palestrante_sessao.text()
        sessao.horario_sessao = participante_ui.txt_horario_sessao.text()
        sessao.nome_evento = participante_ui.cb_tipo_evento_sessao.currentText()
        evento_nome = participante_ui.cb_tipo_evento_sessao.currentText()
        hora = sessao.horario_sessao
        hora = datetime.strptime(hora, '%H:%M').time()
        sessao.horario_sessao = hora
        try:
            evento_id = self.evento_repository.select_evento_by_nome_return_id(evento_nome)
            print(
                f"Inserting Sessao - Tema: {sessao.tema}, Palestrante: {sessao.palestrante}, ID: {evento_id}, Evento Nome: {evento_nome}")

            if evento_id is not None:
                sessao.evento_id = evento_id
                evento = self.evento_repository.select_evento_by_id(evento_id)
                if evento is not None:
                    self.sessao_repository.insert_sessao(sessao, evento)
                    participante_ui.txt_tema_sessao.setText('')
                    participante_ui.txt_palestrante_sessao.setText('')
                    participante_ui.txt_horario_sessao.setText('')
                    self.service_main_window.populate_table_sessao(participante_ui)
                    QMessageBox.information(participante_ui, 'Sessao', 'Sessao cadastrada com sucesso!')
                else:
                    QMessageBox.warning(participante_ui, 'Sessao', 'Evento não encontrado!')
            else:
                QMessageBox.warning(participante_ui, 'Sessao', 'Evento não encontrado!')
        except Exception as e:
            QMessageBox.warning(participante_ui, 'Sessao', f'Erro ao cadastrar sessao! \nErro: {e}')
