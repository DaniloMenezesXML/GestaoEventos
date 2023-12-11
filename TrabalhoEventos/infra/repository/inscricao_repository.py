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
    def select_all_inscricao():
        try:
            with DBConnectionHandler() as db:
                results = (
                    db.session.query(
                        Inscricao,
                        Participante,
                        Evento,
                        Sessao
                    )
                    .join(Participante, Inscricao.participante_id == Participante.id)
                    .join(Evento, Inscricao.evento_id == Evento.id)
                    .join(Sessao, Inscricao.sessao_id == Sessao.id)
                    .all()
                )
                return results
        except Exception as e:
            print(f"Erro ao carregar lista de participantes!\nErro: {e}")

    @staticmethod
    def select_all_inscricao_by_email(email):
        try:
            with DBConnectionHandler() as db:
                results = (
                    db.session.query(
                        Inscricao,
                        Participante,
                        Evento,
                        Sessao
                    )
                    .join(Participante, Inscricao.participante_id == Participante.id)
                    .join(Evento, Inscricao.evento_id == Evento.id)
                    .join(Sessao, Inscricao.sessao_id == Sessao.id)
                    .filter(Participante.email == email).all())
                return results
        except Exception as e:
            print(f"Erro ao carregar lista de participantes!\nErro: {e}")


    @staticmethod
    def select_inscricao_by_id(evento_id, participante_id, sessao_id):
        with DBConnectionHandler() as db:
            inscricao = db.session.query(Inscricao).filter(Inscricao.id == evento_id == participante_id == sessao_id).first()
            if inscricao:
                return inscricao.id
            else:
                return None

    @staticmethod
    def delete_inscricao(id):
        with DBConnectionHandler() as db:
            try:
                inscricao = db.session.query(Inscricao).get(id)
                if inscricao:
                    db.session.delete(inscricao)
                    db.session.commit()
                    print("Inscrição excluída com sucesso!")
                else:
                    print("Inscrição não encontrada para exclusão.")
            except Exception as e:
                print(f"Erro ao excluir a inscrição: {e}")

    @staticmethod
    def select_inscicao_by_email(email_participante):
        with DBConnectionHandler() as db:
            participante = db.session.query(Participante).filter(Participante.inscricao == email_participante).first()
            return participante.inscricao.id
