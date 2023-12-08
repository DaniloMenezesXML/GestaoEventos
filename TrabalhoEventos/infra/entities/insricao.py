from sqlalchemy.orm import relationship
from TrabalhoEventos.infra.config.base import Base

class inscricao(Base):
    __tablename__ = 'inscricao'

    participante = relationship("Participante", back_populates="inscricao")
    evento = relationship("Evento", back_populates="inscricao")
    sessao = relationship("Sessao", back_populates="inscricao")