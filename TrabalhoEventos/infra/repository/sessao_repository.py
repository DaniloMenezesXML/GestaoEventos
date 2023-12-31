from datetime import datetime

from sqlalchemy.orm import joinedload

from TrabalhoEventos.infra.config.connection import DBConnectionHandler
from TrabalhoEventos.infra.entities.participante import Participante
from TrabalhoEventos.infra.entities.evento import Evento
from TrabalhoEventos.infra.entities.sessao import Sessao

class SessaoRepository:

    @staticmethod
    def select_sessao_by_id(id_sessao):
        with DBConnectionHandler() as db:
            sessao = not db.session.query(Sessao).filter(Sessao.id == id_sessao).first()
            return sessao



    @staticmethod
    def insert_sessao(sessao, evento):
        with DBConnectionHandler() as db:

            sessao.evento_id = evento.id

            try:
                db.session.add(sessao, evento)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def select_sessoes_ativos():
        with DBConnectionHandler() as db:
            sessoes = (db.session.query(Sessao, Participante, Evento)
                          .join(Participante, Participante.id == Sessao.participante_id)
                          .join(Evento, Evento.id == Sessao.evento_id)
                       .filter(Sessao.data_sessao.is_(None)).all())
            return sessoes

    @staticmethod
    def select_all_sessoes():
        with DBConnectionHandler() as db:
            sessoes = db.session.query(Sessao).all()
            return sessoes

    @staticmethod
    def select_sessoes_by_email(email):
        try:
            email_participante = email
            with DBConnectionHandler() as db:
                sessoes = (
                    db.session.query(Sessao, Participante, Evento)
                    .join(Participante, Participante.id == Sessao.participante_id)
                    .join(Evento, Evento.id == Sessao.evento_id)
                    .filter(Sessao.tema.between(email_participante))
                    .options(
                        joinedload(Sessao.participante),
                        joinedload(Sessao.evento))
                    .all()
                )
                return sessoes
        except Exception as e:
            print(e)

    @staticmethod
    def select_sessao_by_tema(tema_sessao):
        with DBConnectionHandler() as db:
            sessao = db.session.query(Sessao).filter(Sessao.tema == tema_sessao).first()
            return sessao

    @staticmethod
    def select_sessao_by_tema_return_id(tema_sessao):
        with DBConnectionHandler() as db:
            sessao = db.session.query(Sessao).filter(Sessao.tema == tema_sessao).first()
            if sessao:
                return sessao.id
            else:
                return None
