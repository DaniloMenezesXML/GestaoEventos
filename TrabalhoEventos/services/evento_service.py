from datetime import datetime
from PySide6.QtWidgets import QMessageBox
from TrabalhoEventos.infra.entities.evento import Evento
from TrabalhoEventos.infra.repository.evento_repository import EventoRepository
from TrabalhoEventos.infra.repository.participante_repository import ParticipanteRepository
from TrabalhoEventos.infra.repository.sessao_repository import SessaoRepository
from TrabalhoEventos.services.main_window_service import MainWindowService


class EventoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()
        self.sessao_repository = SessaoRepository()

    def insert_evento(self, main_window):
        evento = Evento()
        evento.nome = main_window.txt_nome_evento.text()
        evento.data_evento = main_window.txt_data_evento.text()
        evento.horario_evento = main_window.txt_horario_evento.text()
        data = evento.data_evento
        data = datetime.strptime(data, '%d/%m/%Y').date()
        hora = evento.horario_evento
        hora = datetime.strptime(hora, '%H:%M').time()
        evento.data_evento = data
        evento.horario_evento = hora

        try:
            self.evento_repository.insert_one_evento(evento)
            main_window.txt_nome_evento.setText('')
            main_window.txt_data_evento.setText('')
            main_window.txt_horario_evento.setText('')

            self.service_main_window.populate_table_evento(main_window)
            QMessageBox.information(main_window, 'Evento', 'Evento cadastrado com sucesso!')
        except Exception as e:
            QMessageBox.warning(main_window, 'Evento', f'Erro ao cadastrar evento! \nErro: {e}')






