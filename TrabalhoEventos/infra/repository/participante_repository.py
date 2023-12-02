from infra.config.connection import DBConnectionHandler
from infra.entities.participante import Participante

class ParticipanteRepository():

    @staticmethod
    def select_participante_by_id(id_participante):
        with DBConnectionHandler() as db:
            participante = not db.session.query(Participante).filter(Participante.id == id_participante).first()
            return participante

    @staticmethod
    def select_funcionario_by_uniforme_id(id_uniforme):
        with DBConnectionHandler() as db:
            funcionario = db.session.query(Funcionario).filter(Funcionario.uniforme_id == id_uniforme).first()
            return funcionario

    @staticmethod
    def select_participante_by_email(email_participante):
        with DBConnectionHandler() as db:
            participante = db.session.query(Participante).filter(Participante.cpf == email_participante).first()
            return participante

    @staticmethod
    def select_all_participante():
        with DBConnectionHandler() as db:
            participante = db.session.query(Participante).all()
            return participante

    @staticmethod
    def select_first_participante():
        with DBConnectionHandler() as db:
            participante = db.session.query(Participante).first()
            return participante

    @staticmethod
    def insert_one_participante(participante):
        with DBConnectionHandler() as db:
            db.session.add(participante)
            db.session.commit()

    @staticmethod
    def insert_many_participante(participante):
        with DBConnectionHandler() as db:
            db.session.add(participante)
            db.session.commit()

    @staticmethod
    def update_participante(participante):
        with DBConnectionHandler() as db:
            db.session.query(Participante).filter(Participante.id == participante.id).update({'nome': participante.nome, 'e-mail': participante.email, 'eventos inscritos': participante.lista_eventos_inscritos})
            db.session.commit()

    @staticmethod
    def delete_participante(participante):
        with DBConnectionHandler() as db:
            db.session.query(Participante).filter(Participante.id == participante.id).update({'ativo': False})
            db.session.commit()
