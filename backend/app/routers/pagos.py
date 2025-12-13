from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import PagoCreate, PagoUpdate, PagoOut
from app.crud.pago import (
    crear_pago, obtener_pago, obtener_todos,
    actualizar_pago, eliminar_pago
)
from app.auth import get_current_user
from app.errors import error_not_found

router = APIRouter(prefix='/pagos', tags=['Pagos'])

@router.post('/', response_model=PagoOut)
def api_crear_pago(data: PagoCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crear_pago(db, data)

@router.get('/', response_model=list[PagoOut])
def api_listar_pagos(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return obtener_todos(db)

@router.get('/{id}', response_model=PagoOut)
def api_obtener_pago(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    pago = obtener_pago(db, id)
    if not pago:
        error_not_found('Pago')
    return pago

@router.put('/{id}', response_model=PagoOut)
def api_actualizar_pago(id: int, data: PagoUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    p = actualizar_pago(db, id, data)
    if not p:
        error_not_found('Pago')
    return p

@router.delete('/{id}')
def api_eliminar_pago(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = eliminar_pago(db, id)
    if not ok:
        error_not_found('Pago')
    return {'mensaje': 'Pago eliminado'}
