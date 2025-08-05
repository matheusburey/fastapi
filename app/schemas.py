from app.models import TipoPerguntaEnum
from pydantic import BaseModel
from typing import Optional, List


class OpcoesRespostaPerguntaBase(BaseModel):
    resposta: str
    ordem: int
    resposta_aberta: Optional[bool] = False


class PerguntaBase(BaseModel):
    titulo: str
    codigo: Optional[str] = None
    orientacao_resposta: Optional[str] = None
    ordem: int
    obrigatoria: bool
    sub_pergunta: bool
    tipo_pergunta: TipoPerguntaEnum


class PerguntaCreate(PerguntaBase):
    id_formulario: int
    opcoes_respostas: List[OpcoesRespostaPerguntaBase] = []


class Pergunta(PerguntaBase):
    id: int
    opcoes_respostas: List[OpcoesRespostaPerguntaBase]

    class Config:
        orm_mode = True


class FormularioBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ordem: int


class FormularioCreate(FormularioBase):
    pass


class Formulario(FormularioBase):
    id: int
    perguntas: List[Pergunta] = []

    class Config:
        orm_mode = True
