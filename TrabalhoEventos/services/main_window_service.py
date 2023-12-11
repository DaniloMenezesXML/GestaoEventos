import datetime

import pandas as pd
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from TrabalhoEventos.infra.repository.evento_repository import EventoRepository
from TrabalhoEventos.infra.repository.participante_repository import ParticipanteRepository
from TrabalhoEventos.infra.repository.sessao_repository import SessaoRepository
from TrabalhoEventos.infra.repository.inscricao_repository import InscricaoRepository


class MainWindowService:
    def __init__(self):
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()
        self.sessao_repository = SessaoRepository()
        self.inscricao_repository = InscricaoRepository()
    def populate_table_sessao(self, main_window):
        main_window.tb_lista_sessao_criar_sessao.setRowCount(0)
        lista_sessao = self.sessao_repository.select_all_sessoes()
        main_window.tb_lista_sessao_criar_sessao.setRowCount(len(lista_sessao))
        for linha, sessao in enumerate(lista_sessao):
            main_window.tb_lista_sessao_criar_sessao.setItem(linha, 0, QTableWidgetItem(sessao.tema))
            main_window.tb_lista_sessao_criar_sessao.setItem(linha, 1, QTableWidgetItem(sessao.palestrante))
            main_window.tb_lista_sessao_criar_sessao.setItem(linha, 2, QTableWidgetItem(sessao.horario_sessao.strftime('%H:%M')))
            main_window.tb_lista_sessao_criar_sessao.setItem(linha, 3, QTableWidgetItem(sessao.nome_evento))
            main_window.tb_lista_sessao_criar_sessao.setItem(linha, 4, QTableWidgetItem(sessao.evento_id))

    def populate_table_evento(self, main_window):
        main_window.tableWidget.setRowCount(0)
        lista_evento = self.evento_repository.select_all_evento()
        main_window.tableWidget.setRowCount(len(lista_evento))
        for linha, evento in enumerate(lista_evento):
            main_window.tableWidget.setItem(linha, 0, QTableWidgetItem(evento.nome))
            main_window.tableWidget.setItem(linha, 1, QTableWidgetItem(evento.data_evento.strftime('%d/%m/%Y')))
            main_window.tableWidget.setItem(linha, 2, QTableWidgetItem(evento.horario_evento.strftime('%H:%M')))

    def populate_table_lista_participante(self, main_window):
        main_window.tb_participante.setRowCount(0)
        lista_participante = self.participante_repository.select_all_participante()
        main_window.tb_participante.setRowCount(len(lista_participante))
        for linha, (participante) in enumerate(lista_participante):
            main_window.tb_participante.setItem(linha, 0, QTableWidgetItem(participante.nome))
            main_window.tb_participante.setItem(linha, 1, QTableWidgetItem(participante.email))


    def populate_sessoes_combo(self, inscricao_ui):
        inscricao_ui.cb_sessao.clear()
        inscricao_ui.cb_sessao.addItem('Selecione')
        inscricao_ui.sessoes = self.sessao_repository.select_all_sessoes()
        for sessao in inscricao_ui.sessoes:
            inscricao_ui.cb_sessao.addItem(sessao.tema)

    def populate_eventos_combo(self, inscricao_ui):
        inscricao_ui.cb_evento.clear()
        inscricao_ui.cb_evento.addItem('Selecione')
        inscricao_ui.eventos = self.evento_repository.select_all_evento()
        for evento in inscricao_ui.eventos:
            inscricao_ui.cb_evento.addItem(evento.nome)

    def populate_eventos_ativos(self, main_window):
        main_window.cb_tipo_evento_sessao.clear()
        main_window.cb_tipo_evento_sessao.addItem('Selecione o evento')
        eventos_ativos = self.evento_repository.select_all_evento()
        for evento in eventos_ativos:
            main_window.cb_tipo_evento_sessao.addItem(evento.nome)

    def update_table_sessao(self, inscricao_ui):
        selected_item_index = inscricao_ui.cb_sessao.currentIndex()
        inscricao_ui.tb_sessao.setRowCount(0)
        if selected_item_index > 0:
            selected_sessao = inscricao_ui.sessoes[selected_item_index - 1]
            for i, sessao in enumerate(selected_sessao.dados):
                inscricao_ui.tb_sessoes.insertRow(i)
                inscricao_ui.tb_sessoes.setItem(i, 0, QTableWidgetItem(f'Tema: {sessao.tema}'
                                                                       f'\nPalestrante: {sessao.palestrante}'))
                inscricao_ui.tb_sessoes.setItem(i, 1, QTableWidgetItem(sessao.horario_sessao
                                                                                      .strftime('%d/%m/%Y_%H:%M:%S')))

    def populate_agenda(self, main_window):
        try:
            main_window.tb_lista_sessao_agenda.setRowCount(0)
            inscricao_email = self.inscricao_repository.select_all_inscricao_by_email(main_window.txt_email_participante_agenda.text())
            main_window.tb_lista_sessao_agenda.setRowCount(len(inscricao_email))
            for linha, (inscricao, participante, evento, sessao) in enumerate(inscricao_email):
                main_window.tb_lista_sessao_agenda.setItem(linha, 0, QTableWidgetItem(participante.nome))
                main_window.tb_lista_sessao_agenda.setItem(linha, 1, QTableWidgetItem(evento.nome))
                main_window.tb_lista_sessao_agenda.setItem(linha, 2, QTableWidgetItem(sessao.tema))
                main_window.tb_lista_sessao_agenda.setItem(linha, 3, QTableWidgetItem(sessao.horario_sessao
                                                                                      .strftime('%H:%M')))
        except Exception as e:
            QMessageBox.warning(main_window, 'Atenção', f'E-mail inserido pode estar incorreto!\nErro {e}')

    def populate_table_lista_participante_inicio(self, main_window):
        try:
            main_window.tb_lista_participante_inicio.setRowCount(0)
            lista_inscricao = self.inscricao_repository.select_all_inscricao()
            main_window.tb_lista_participante_inicio.setRowCount(len(lista_inscricao))
            for linha, (inscricao, participante, evento, sessao) in enumerate(lista_inscricao):
                main_window.tb_lista_participante_inicio.insertRow(linha)
                main_window.tb_lista_participante_inicio.setItem(linha, 0, QTableWidgetItem(participante.nome))
                main_window.tb_lista_participante_inicio.setItem(linha, 1, QTableWidgetItem(participante.email))
                main_window.tb_lista_participante_inicio.setItem(linha, 2, QTableWidgetItem(evento.nome))
                main_window.tb_lista_participante_inicio.setItem(linha, 3, QTableWidgetItem(sessao.tema))
        except Exception as e:
            QMessageBox.warning(main_window, 'Atenção', f'Erro ao carregar lista de participantes!\nErro: {e}')
