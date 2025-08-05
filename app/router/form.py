from fastapi import APIRouter, Depends, HTTPException, Query
from app import schemas
from app.crud import form as crud
from app.database import get_db
from sqlalchemy.orm import Session
from typing import List, Optional


router = APIRouter(prefix="/formularios", tags=["Formularios"])


@router.post("/", response_model=schemas.Formulario)
def create_formulario(
    formulario: schemas.FormularioCreate, db: Session = Depends(get_db)
):
    """Cria um novo formulario."""
    return crud.create_formulario(db, formulario)


@router.get("/", response_model=List[schemas.Formulario])
def read_formularios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Lista todos os formularios."""
    return crud.get_formularios(db, skip=skip, limit=limit)


@router.get("/{formulario_id}", response_model=schemas.Formulario)
def read_formulario(formulario_id: int, db: Session = Depends(get_db)):
    """Lista um formulario."""
    db_formulario = crud.get_formulario(db, formulario_id)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulario not found")
    return db_formulario


@router.put("/{formulario_id}", response_model=schemas.Formulario)
def update_formulario(
    formulario_id: int,
    formulario: schemas.FormularioCreate,
    db: Session = Depends(get_db),
):
    """Atualiza um formulario."""
    return crud.update_formulario(db, formulario_id, formulario)


@router.delete("/{formulario_id}")
def delete_formulario(formulario_id: int, db: Session = Depends(get_db)):
    """Deleta um formulario."""
    crud.delete_formulario(db, formulario_id)
    return {"ok": True}


@router.get("/{formulario_id}/perguntas", response_model=List[schemas.Pergunta])
def list_perguntas_formulario(
    formulario_id: int,
    tipo_pergunta: Optional[schemas.TipoPerguntaEnum] = Query(None),
    obrigatoria: Optional[bool] = Query(None),
    order_by: str = Query("ordem"),
    order_dir: str = Query("asc"),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    """Lista as perguntas de um formulario."""
    return crud.list_perguntas_formulario(
        db, formulario_id, tipo_pergunta, obrigatoria, order_by, order_dir, skip, limit
    )
