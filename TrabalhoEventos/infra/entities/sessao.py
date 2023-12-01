from __future__ import  annotations
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base

class Sessao(Base):
    __tablename__ = 'sessão'

    participante_id: Mapped[int] = mapped_column(ForeignKey("participante.id"), primary_key=True)
    evento_id: Mapped[int] = mapped_column(ForeignKey("evento.id"), primary_key=True)
    data_sessao: Mapped[datetime] = mapped_column(nullable=False)

    participante = relationship("Participante", back_populates= "sessão")
    evento = relationship("Evento", back_populates= "sessão")