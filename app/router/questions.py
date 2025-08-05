from fastapi import APIRouter, Depends, HTTPException
from app import schemas
from app.crud import questions as crud
from app.database import get_db
from sqlalchemy.orm import Session


router = APIRouter(prefix="/perguntas", tags=["Perguntas"])


@router.post("/", response_model=schemas.Pergunta)
def create_pergunta(pergunta: schemas.PerguntaCreate, db: Session = Depends(get_db)):
    """Cria uma nova pergunta."""
    return crud.create_pergunta(db, pergunta)


@router.get("/{pergunta_id}", response_model=schemas.Pergunta)
def read_pergunta(pergunta_id: int, db: Session = Depends(get_db)):
    """Lista uma pergunta."""
    db_pergunta = crud.get_pergunta(db, pergunta_id)
    if db_pergunta is None:
        raise HTTPException(status_code=404, detail="Pergunta not found")
    return db_pergunta


@router.put("/{pergunta_id}", response_model=schemas.Pergunta)
def update_pergunta(
    pergunta_id: int, pergunta: schemas.PerguntaCreate, db: Session = Depends(get_db)
):
    """Atualiza uma pergunta."""
    return crud.update_pergunta(db, pergunta_id, pergunta)


@router.delete("/{pergunta_id}")
def delete_pergunta(pergunta_id: int, db: Session = Depends(get_db)):
    """Deleta uma pergunta."""
    crud.delete_pergunta(db, pergunta_id)
    return {"ok": True}
