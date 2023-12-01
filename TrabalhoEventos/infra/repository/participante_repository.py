from infra.config.connection import DBConnectionHandler
from infra.entities import participante

class ParticipanteRepository:

    @staticmethod
    def select_participante_by_id(id_participante):
        with DBConnectionHandler() as db:
            participante = db.session.query(Participante).filter(Participante.id == id_participante).first

            return participante

    @staticmethod
    def insert_one_participante(participante):
        with DBConnectionHandler() as db:
            db.session.add(participante)
            db.session.commit()

    @staticmethod
    def delete_participante(participante):
        with DBConnectionHandler() as db:
            db.session.query(participante).filter(Participante.id == participante.id).update({'ativo': False})
            db.session.commit()

