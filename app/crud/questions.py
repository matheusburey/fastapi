from sqlalchemy.orm import Session
from app import models, schemas


def create_pergunta(db: Session, pergunta: schemas.PerguntaCreate):
    pergunta_dict = pergunta.model_dump()
    opcoes_resposta_pergunta = pergunta_dict.pop("opcoes_respostas")

    db_pergunta = models.Pergunta(**pergunta_dict)
    db.add(db_pergunta)
    db.commit()
    db.refresh(db_pergunta)

    for opcao in opcoes_resposta_pergunta:
        opcao["id_pergunta"] = db_pergunta.id
        db.add(models.OpcoesResposta(**opcao))

    db.commit()
    return db_pergunta


def get_pergunta(db: Session, pergunta_id: int):
    return db.query(models.Pergunta).filter(models.Pergunta.id == pergunta_id).first()


def update_pergunta(db: Session, pergunta_id: int, pergunta: schemas.PerguntaCreate):
    db_pergunta = get_pergunta(db, pergunta_id)
    for key, value in pergunta.model_dump().items():
        setattr(db_pergunta, key, value)
    db.commit()
    db.refresh(db_pergunta)
    return db_pergunta


def delete_pergunta(db: Session, pergunta_id: int):
    db_pergunta = get_pergunta(db, pergunta_id)
    db.delete(db_pergunta)
    db.commit()
