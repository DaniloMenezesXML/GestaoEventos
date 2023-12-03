from __future__ import  annotations
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from TrabalhoEventos.infra.config.base import Base

class Sessao(Base):
    __tablename__ = 'sessao'

    participante_id: Mapped[int] = mapped_column(ForeignKey("participante.id"), primary_key=True)
    evento_id: Mapped[int] = mapped_column(ForeignKey("evento.id"), primary_key=True)
    tema: Mapped[str] = mapped_column(nullable=False)
    palestrante: Mapped[str] = mapped_column(nullable=False)
    data_sessao: Mapped[datetime] = mapped_column(nullable=False)

    participante = relationship("Participante", back_populates= "sessao")
    evento = relationship("Evento", back_populates= "sessao")

    def __repr__(self):
        return (f'Sessao [tema= {self.nome}, palestrante={self.palestrante},'
                f' data da sessao= {self.data_sessao}]')
