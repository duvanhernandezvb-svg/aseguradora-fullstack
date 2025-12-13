from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import SiniestroCreate, SiniestroUpdate, SiniestroOut
from app.crud.siniestro import (
    crear_siniestro, obtener_siniestro, obtener_todos,
    actualizar_siniestro, eliminar_siniestro
)
from app.auth import get_current_user
from app.errors import error_not_found

router = APIRouter(prefix='/siniestros', tags=['Siniestros'])

@router.post('/', response_model=SiniestroOut)
def api_crear_siniestro(data: SiniestroCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crear_siniestro(db, data)

@router.get('/', response_model=list[SiniestroOut])
def api_listar_siniestros(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return obtener_todos(db)

@router.get('/{id}', response_model=SiniestroOut)
def api_obtener_siniestro(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    s = obtener_siniestro(db, id)
    if not s:
        error_not_found('Siniestro')
    return s

@router.put('/{id}', response_model=SiniestroOut)
def api_actualizar_siniestro(id: int, data: SiniestroUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    s = actualizar_siniestro(db, id, data)
    if not s:
        error_not_found('Siniestro')
    return s

@router.delete('/{id}')
def api_eliminar_siniestro(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = eliminar_siniestro(db, id)
    if not ok:
        error_not_found('Siniestro')
    return {'mensaje': 'Siniestro eliminado'}
