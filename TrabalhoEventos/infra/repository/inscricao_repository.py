from TrabalhoEventos.infra.config.connection import DBConnectionHandler
from TrabalhoEventos.infra.entities.evento import Evento
from TrabalhoEventos.infra.entities.inscricao import Inscricao
from TrabalhoEventos.infra.entities.participante import Participante
from TrabalhoEventos.infra.entities.sessao import Sessao


class InscricaoRepository():

    @staticmethod
    def insert_inscricao(participante_id, evento_id, sessao_id, inscricao):
        with DBConnectionHandler() as db:
            insc = Inscricao()
            insc.evento_id = evento_id
            insc.participante_id = participante_id
            insc.sessao_id = sessao_id
            try:
                db.session.add(insc)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def select_inscricao_by_id_return_id(evento_id, participante_id, sessao_id):
        with DBConnectionHandler() as db:
            evento = db.session.query(Evento).filter(Evento.id == evento_id).first()
            participante = db.session.query(Participante).filter(Participante.id == participante_id).first()
            sessao = db.session.query(Sessao).filter(Sessao.id == sessao_id).first()
            inscricao = db.session.query(Sessao).filter(Sessao.id == sessao_id).first()
            if inscricao:
                return inscricao
            else:
                return None

    @staticmethod
    def delete_inscricao(participante_id, evento_id, sessao_id, inscricao):
        with DBConnectionHandler() as db:
            insc = Inscricao()
            insc.evento_id = evento_id
            insc.participante_id = participante_id
            insc.sessao_id = sessao_id
            try:
                db.session.delete(insc)
                db.session.commit()
            except Exception as e:
                print(e)