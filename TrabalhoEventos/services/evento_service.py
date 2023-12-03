from PySide6.QtWidgets import QMessageBox

from infra.entities import evento
from infra.repository import evento_repository

from services.main_window_service import MainWindowService


class EventoService:
    def __init__(self):
        self.service_main_window = MainWindowService()
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()
        self.sessao_repository = SessaoRepository()

    def insert_evento(self, main_window):
        evento = Evento()
        evento.nome = main_window.txt_nome_evento.text()
        evento.data = main_window.txt_data_evento.text()
        evento.horario = main_window.txt_horario_evento.text()

        try:
            self.evento_repository.insert_evento(evento)
            main_window.txt_nome_evento.setText('')
            main_window.txt_data_evento.setText('')
            main_window.txt_horario_evento.setText('')

            self.service_main_window.populate_table_evento(main_window)
            QMessageBox.information(main_window, 'Evento', 'Evento cadastrado com sucesso!')
        except Exception as e:
            QMessageBox.warning(main_window, 'Evento', f'Erro ao cadastrar evento! \nErro: {e}')







