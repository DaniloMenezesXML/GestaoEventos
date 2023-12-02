from __future__ import  annotations
from sqlalchemy.orm import Mapped, mapped_column, relationship
from infra.config.base import Base

class Participante(Base):
    __tablename__ = 'participante'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    lista_inscritos: Mapped[list] = mapped_column(nullabe=False)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    sessao = relationship("Sessao", back_populates="participante", cascade="save-update")

    def __repr__(self):
        return (f'Participante [nome= {self.nome}, e-mail= {self.email},'
                f' eventos inscritos{self.lista_inscritos}]')
