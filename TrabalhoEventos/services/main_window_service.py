import datetime

import pandas as pd
from PySide6.QtWidgets import QMessageBox, QTableWidgetItem

from TrabalhoEventos.infra.repository.evento_repository import EventoRepository
from TrabalhoEventos.infra.repository.participante_repository import ParticipanteRepository
from TrabalhoEventos.infra.repository.sessao_repository import SessaoRepository


class MainWindowService:
    def __init__(self):
        self.evento_repository = EventoRepository()
        self.participante_repository = ParticipanteRepository()
        self.sessao_repository = SessaoRepository()

    def populate_table_sessao(self, main_window):
        main_window.tb_lista_sessao_criar_sessao.setRowCount(0)
        lista_sessao = self.sessao_repository.select_all_sessoes()
        main_window.tb_lista_sessao_criar_sessao.setRowCount(len(lista_sessao))
        for linha, sessao in enumerate(lista_sessao):
            if sessao.ativo:
                main_window.tb_lista_sessao_criar_sessao.setItem(linha, 0, QTableWidgetItem(sessao.tema))
                main_window.tb_lista_sessao_criar_sessao.setItem(linha, 1, QTableWidgetItem(sessao.palestrante))
                main_window.tb_lista_sessao_criar_sessao.setItem(linha, 2, QTableWidgetItem(sessao.horario_sessao.strftime('%H:%M:%S')))
                main_window.tb_lista_sessao_criar_sessao.setItem(linha, 3, QTableWidgetItem(sessao.evento))

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

    def populate_eventos_ativos(self, emprestimo_ui):
        emprestimo_ui.cb_tipo_evento_sessao.clear()
        emprestimo_ui.cb_tipo_evento_sessao.addItem('Selecione o evento')
        eventos_ativos = self.evento_repository.select_all_evento()
        for evento in eventos_ativos:
            emprestimo_ui.cb_tipo_evento_sessao.addItem(evento.nome)

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
            sessoes = self.sessao_repository.select_sessoes_by_email(main_window.txt_email_participante_agenda.text())
            main_window.tb_lista_sessao_agenda.setRowCount(len(sessoes))
            for linha, (ses, participante, evento) in enumerate(sessoes):
                main_window.tb_lista_sessao_agenda.setItem(linha, 0, QTableWidgetItem(participante.nome))
                main_window.tb_lista_sessao_agenda.setItem(linha, 1, QTableWidgetItem(evento.nome))
                main_window.tb_lista_sessao_agenda.setItem(linha, 2, QTableWidgetItem(ses.tema))
                main_window.tb_lista_sessao_agenda.setItem(linha, 3, QTableWidgetItem(ses.horario_sessao
                                                                                      .strftime('%d/%m/%Y_%H:%M:%S')))
        except Exception as e:
            QMessageBox.warning(main_window, 'Atenção', f'E-mail inserido pode estar incorreto!\nErro {e}')

    def export_agenda(self, main_window):
        if main_window.tb_lista_sessao_agenda.rowCount() > 0:
            rows = main_window.tb_lista_sessao_agenda.rowCount()
            cols = main_window.tb_lista_sessao_agenda.columnCount()
            headers = ['Nome do participante', 'Evento', 'Sessão', 'Horário da Sessão']
            data = []
            for row in range(rows):
                row_data = []
                for col in range(cols):
                    item = main_window.tb_lista_sessao_agenda.item(row, col)
                    if item and item.text():
                        row_data.append(item.text())
                    else:
                        row_data.append('')
                data.append(row_data)
            try:
                df = pd.DataFrame(data, columns=headers)
            except Exception as e:
                pass

            try:
                df.to_excel(f'relatorio_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.xlsx', index=False,
                            engine='openpyxl')
                QMessageBox.information(main_window, "sesréstimos", f'Relatório exportado com sucesso! \n'
                                                                    f'Verifique na pasta do programa o arquivo:\n'
                                                                    f' relarorio_{datetime.datetime.now()}.xlsx')
            except Exception as e:
                QMessageBox.warning(main_window, 'Atenção', f'Erro ao gerar relatório!\nErro: {e}')
