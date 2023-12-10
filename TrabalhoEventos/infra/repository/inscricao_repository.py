from TrabalhoEventos.infra.config.connection import DBConnectionHandler
from TrabalhoEventos.infra.entities.inscricao import Inscricao

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