from __future__ import  annotations

from datetime import time

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from TrabalhoEventos.infra.config.base import Base

class Inscricao(Base):
    __tablename__ = 'inscricao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    evento_id: Mapped[int] = mapped_column(ForeignKey("evento.id"))
    sessao_id: Mapped[int] = mapped_column(ForeignKey("sessao.id"))
    participante_id: Mapped[int] = mapped_column(ForeignKey("participante.id"))
    tema: Mapped[str] = mapped_column(nullable=False)
    palestrante: Mapped[str] = mapped_column(nullable=False)
    horario_sessao: Mapped[time] = mapped_column(nullable=False)
    nome_evento: Mapped[str] = mapped_column(nullable=False)

    participante = relationship("Participante", back_populates="inscricao")
    evento = relationship("Evento", back_populates="inscricao")
    sessao = relationship("Sessao", back_populates="inscricao")

    def __repr__(self):
        return