from sqlalchemy.orm import relationship, mapped_column, Mapped
from sqlalchemy import ForeignKey
from TrabalhoEventos.infra.config.base import Base
from datetime import date, time

class Evento(Base):
    __tablename__ = 'evento'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    data_evento: Mapped[date] = mapped_column(nullable=False)
    sessao: Mapped[int] = relationship("Sessao", back_populates="evento", cascade="save-update")
    horario_evento: Mapped[time] = mapped_column(nullable=False)

    def __repr__(self):
        return (f'Evento [nome= {self.nome}, data do evento= {self.data_evento}, horário do evento= {self.horario_evento}]')

class Participante(Base):
    __tablename__ = 'participante'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)

    sessao_id: Mapped[int] = mapped_column(ForeignKey("sessao.id"), nullable=False)
    sessao: Mapped[int] = relationship("Sessao", back_populates="participante")

    def __repr__(self):
        return (f'Participante [nome= {self.nome}, e-mail= {self.email}]')

class Sessao(Base):
    __tablename__ = 'sessao'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    evento_id: Mapped[int] = mapped_column(ForeignKey("evento.id"), nullable=False)
    tema: Mapped[str] = mapped_column(nullable=False)
    palestrante: Mapped[str] = mapped_column(nullable=False)
    horario_sessao: Mapped[time] = mapped_column(nullable=False)

    evento: Mapped[int] = relationship("Evento", back_populates="sessao")
    participantes: Mapped[int] = relationship("Participante", back_populates="sessao")  # Adicione esta linha
    inscricoes: Mapped[int] = relationship("Inscricao", back_populates="sessao")  # Adicionado

    def __repr__(self):
        return (f'Sessao [tema= {self.tema}, palestrante={self.palestrante},'
                f' horário da sessao= {self.horario_sessao}]')

class Inscricao(Base):
    __tablename__ = 'inscricao'

    participante_id: Mapped[int] = mapped_column(ForeignKey("participante.id"), primary_key=True)
    evento_id: Mapped[int] = mapped_column(ForeignKey("evento.id"), primary_key=True)
    sessao_id: Mapped[int] = mapped_column(ForeignKey("sessao.id"), primary_key=True)

    participante: Mapped[int] = relationship("Participante", back_populates="inscricao")
    evento: Mapped[int] = relationship("Evento", back_populates="inscricao")
    sessao: Mapped[int] = relationship("Sessao", back_populates="inscricao")
