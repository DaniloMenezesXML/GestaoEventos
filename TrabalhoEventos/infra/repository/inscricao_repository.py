from TrabalhoEventos.infra.config.connection import DBConnectionHandler
from TrabalhoEventos.infra.entities.inscricao import Inscricao

class InscricaoRepository():

    @staticmethod
    def insert_inscricao(self, participante, evento, sessao):
        with DBConnectionHandler() as db:
            insc = Inscricao()
            insc.evento_id = evento.id
            insc.participante_id = participante.id
            insc.sessao_id = sessao.id
            try:
                db.session.add(insc)
                db.session.commit()
            except Exception as e:
                print(e)

