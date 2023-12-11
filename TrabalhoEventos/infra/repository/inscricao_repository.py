from TrabalhoEventos.infra.config.connection import DBConnectionHandler
from TrabalhoEventos.infra.entities.inscricao import Inscricao
from TrabalhoEventos.infra.entities.participante import Participante
from TrabalhoEventos.infra.entities.evento import Evento
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
    def select_all_inscricao():
        try:
            with DBConnectionHandler() as db:
                inscricoes = (
                    db.session.query(
                        Inscricao,
                        Participante.nome.label('participante_nome'),
                        Participante.email.label('participante_email'),
                        Evento.nome.label('evento_nome'),
                        Sessao.tema.label('sessao_tema')
                    )
                    .join(Participante, Inscricao.participante_id == Participante.id)
                    .join(Evento, Inscricao.evento_id == Evento.id)
                    .join(Sessao, Inscricao.sessao_id == Sessao.id)
                    .all()
                )
                return inscricoes
        except Exception as e:
            print(e)
