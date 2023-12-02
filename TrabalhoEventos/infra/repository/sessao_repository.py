from datetime import datetime

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
    def insert_sessao(participante, evento):
        with DBConnectionHandler() as db:
            ses = Sessao()
            ses.evento_id = evento.id
            ses.participante_id = participante.id
            today = datetime.now()
            ses.data_sessao = today

            try:
                db.session.add(ses)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def select_sessoes_ativos():
        with DBConnectionHandler() as db:
            sessoes = (db.session.query(Sessao, Participante, Evento)
                          .join(Participante, Participante.id == Sessao.participante_id)
                          .join(Evento, Evento.id == Sessao.evento_id))
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