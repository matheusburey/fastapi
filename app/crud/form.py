from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import asc, desc


def create_formulario(db: Session, formulario: schemas.FormularioCreate):
    db_formulario = models.Formulario(**formulario.model_dump())
    db.add(db_formulario)
    db.commit()
    db.refresh(db_formulario)
    return db_formulario


def get_formulario(db: Session, formulario_id: int):
    return (
        db.query(models.Formulario)
        .filter(models.Formulario.id == formulario_id)
        .first()
    )


def get_formularios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Formulario).offset(skip).limit(limit).all()


def update_formulario(
    db: Session, formulario_id: int, formulario: schemas.FormularioCreate
):
    db_formulario = get_formulario(db, formulario_id)
    for key, value in formulario.model_dump().items():
        setattr(db_formulario, key, value)
    db.commit()
    db.refresh(db_formulario)
    return db_formulario


def delete_formulario(db: Session, formulario_id: int):
    db_formulario = get_formulario(db, formulario_id)
    db.delete(db_formulario)
    db.commit()


def list_perguntas_formulario(
    db: Session,
    formulario_id: int,
    tipo_pergunta: schemas.TipoPerguntaEnum = None,
    obrigatoria: bool = None,
    order_by: str = "ordem",
    order_dir: str = "asc",
    skip: int = 0,
    limit: int = 10,
):
    query = db.query(models.Pergunta).filter(
        models.Pergunta.id_formulario == formulario_id
    )

    if tipo_pergunta:
        query = query.filter(models.Pergunta.tipo_pergunta == tipo_pergunta)

    if obrigatoria is not None:
        query = query.filter(models.Pergunta.obrigatoria == obrigatoria)

    if order_dir == "asc":
        query = query.order_by(asc(getattr(models.Pergunta, order_by)))
    else:
        query = query.order_by(desc(getattr(models.Pergunta, order_by)))

    return query.offset(skip).limit(limit).all()
