from __future__ import  annotations
from datetime import time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from TrabalhoEventos.infra.config.base import Base

class Sessao(Base):
    __tablename__ = 'sessao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    evento_id: Mapped[int] = mapped_column(ForeignKey("evento.id"), nullable=False)
    tema: Mapped[str] = mapped_column(nullable=False)
    palestrante: Mapped[str] = mapped_column(nullable=False)
    horario_sessao: Mapped[time] = mapped_column(nullable=False)
    nome_evento: Mapped[str] = mapped_column(nullable=False)

    evento = relationship("Evento", back_populates= "sessao")
    inscricao = relationship("Inscricao", back_populates="sessao", cascade="save-update")

    def __repr__(self):
        return (f'Sessao [tema= {self.tema}, palestrante={self.palestrante},'
                f' horário da sessao= {self.horario_sessao}]')
