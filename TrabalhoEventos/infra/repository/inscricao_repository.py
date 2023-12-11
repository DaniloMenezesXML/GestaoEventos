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
    def select_inscricao_by_id(evento_id, participante_id, sessao_id):
        with DBConnectionHandler() as db:
            inscricao = db.session.query(Inscricao).filter(Inscricao.id == evento_id == participante_id == sessao_id).first()
            if inscricao:
                return inscricao.id
            else:
                return None

    @staticmethod
    def delete_inscricao(inscricao):
        with DBConnectionHandler() as db:
            try:
                db.session.delete(inscricao)
                db.session.commit()
            except Exception as e:
                print(e)