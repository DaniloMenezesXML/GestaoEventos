from infra.config.connection import DBConnectionHandler
from infra.entities.evento import Evento

class EventoRepository():

    @staticmethod
    def select_evento_by_id(id_evento):
        with DBConnectionHandler() as db:
            evento = not db.session.query(Evento).filter(Evento.id == id_evento).first()
            return evento

    @staticmethod
    def select_evento_by_participante_id(id_participante):
        with DBConnectionHandler() as db:
            evento = db.session.query(Evento).filter(Evento.participante_id == id_participante).first()
            return evento

    @staticmethod
    def select_evento_by_nome(nome_evento):
        with DBConnectionHandler() as db:
            evento = db.session.query(Evento).filter(Evento.cpf == nome_evento).first()
            return evento

    @staticmethod
    def select_all_evento():
        with DBConnectionHandler() as db:
            evento = db.session.query(Evento).all()
            return evento

    @staticmethod
    def select_first_evento():
        with DBConnectionHandler() as db:
            evento = db.session.query(Evento).first()
            return evento

    @staticmethod
    def insert_one_evento(evento):
        with DBConnectionHandler() as db:
            db.session.add(evento)
            db.session.commit()

    @staticmethod
    def insert_many_evento(evento):
        with DBConnectionHandler() as db:
            db.session.add(evento)
            db.session.commit()

    @staticmethod
    def update_evento(evento):
        with DBConnectionHandler() as db:
            db.session.query(Evento).filter(Evento.id == evento.id).update({'nome': evento.nome, 'data do evento': evento.data_evento, 'lista de participantes': evento.lista_participante})
            db.session.commit()

    @staticmethod
    def delete_evento(evento):
        with DBConnectionHandler() as db:
            db.session.query(Evento).filter(Evento.id == evento.id).update({'ativo': False})
            db.session.commit()
