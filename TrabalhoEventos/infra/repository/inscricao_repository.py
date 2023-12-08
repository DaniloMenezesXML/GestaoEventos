

from TrabalhoEventos.infra.config.connection import DBConnectionHandler
from TrabalhoEventos.infra.entities.evento import Evento
from TrabalhoEventos.infra.entities.sessao import Sessao
from TrabalhoEventos.infra.entities.participante import Participante

class inscricao_repository(Base):

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
