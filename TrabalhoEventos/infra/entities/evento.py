from __future__ import  annotations

import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship
from infra.config.base import Base

class Evento(Base):
    __tablename__ = 'Evento'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    data_evento: Mapped[datetime] = mapped_column(nullable=False)
    lista_participante: Mapped[list] = mapped_column(nullabe=False)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    sessao = relationship("Sessão", back_populates="evento", cascade="save-update")

    def __repr__(self):
        return (f'Evento [nome= {self.nome}, Data do Evento= {self.data_evento},'
                f' Lista de Participantes={self.lista_participante}]')
