from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum


class TipoPerguntaEnum(str, enum.Enum):
    SIM_NAO = "Sim_Nao"
    MULTIPLA_ESCOLHA = "multipla_escolha"
    UNICA_ESCOLHA = "unica_escolha"
    TEXTO_LIVRE = "texto_livre"
    INTEIRO = "Inteiro"
    DECIMAL = "Numero com duas casa decimais"


class Formulario(Base):
    __tablename__ = "formulario"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    ordem = Column(Integer, nullable=False)

    perguntas = relationship("Pergunta", back_populates="formulario")


class Pergunta(Base):
    __tablename__ = "pergunta"

    id = Column(Integer, primary_key=True, index=True)
    id_formulario = Column(Integer, ForeignKey("formulario.id"), nullable=False)
    titulo = Column(String, nullable=False)
    codigo = Column(String, nullable=True)
    orientacao_resposta = Column(String, nullable=True)
    ordem = Column(Integer, nullable=False)
    obrigatoria = Column(Boolean, default=False)
    sub_pergunta = Column(Boolean, default=False)
    tipo_pergunta = Column(Enum(TipoPerguntaEnum), nullable=False)

    formulario = relationship("Formulario", back_populates="perguntas")
    opcoes_respostas = relationship("OpcoesResposta", back_populates="pergunta")
    opcoes_resposta_pergunta = relationship(
        "OpcoesRespostaPergunta", back_populates="pergunta"
    )


class OpcoesResposta(Base):
    __tablename__ = "opcoes_respostas"

    id = Column(Integer, primary_key=True, index=True)
    id_pergunta = Column(Integer, ForeignKey("pergunta.id"), nullable=False)
    resposta = Column(String, nullable=False)
    ordem = Column(Integer, nullable=False)
    resposta_aberta = Column(Boolean, default=False)

    pergunta = relationship("Pergunta", back_populates="opcoes_respostas")


class OpcoesRespostaPergunta(Base):
    __tablename__ = "opcoes_resposta_pergunta"

    id = Column(Integer, primary_key=True, index=True)
    id_opcao_resposta = Column(
        Integer, ForeignKey("opcoes_respostas.id"), nullable=False
    )
    id_pergunta = Column(Integer, ForeignKey("pergunta.id"), nullable=False)

    pergunta = relationship("Pergunta", back_populates="opcoes_resposta_pergunta")
