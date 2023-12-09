from __future__ import  annotations

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from TrabalhoEventos.infra.config.base import Base

class Inscricao(Base):
    __tablename__ = 'inscricao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    evento_id: Mapped[int] = mapped_column(ForeignKey("evento.id"), foreign_key=True)
    sessao_id: Mapped[int] = mapped_column(ForeignKey("sessao.id"), foreign_key=True)
    participante_id: Mapped[int] = mapped_column(ForeignKey("participante.id"), foreign_key=True)

    participante = relationship("Participante", back_populates="inscricao")
    evento = relationship("Evento", back_populates="inscricao")
    sessao = relationship("Sessao", back_populates="inscricao")

    def __repr__(self):
        return