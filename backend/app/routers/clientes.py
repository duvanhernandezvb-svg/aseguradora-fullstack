from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ClienteCreate, ClienteUpdate, ClienteOut
from app.crud.cliente import crear_cliente, obtener_cliente, obtener_todos, actualizar_cliente, eliminar_cliente
from app.auth import get_current_user
from app.errors import error_not_found

router = APIRouter(prefix='/clientes', tags=['Clientes'])

@router.post('/', response_model=ClienteOut)
def api_crear_cliente(data: ClienteCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crear_cliente(db, data)

@router.get('/', response_model=list[ClienteOut])
def api_listar_clientes(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return obtener_todos(db)

@router.get('/{id}', response_model=ClienteOut)
def api_obtener_cliente(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    cliente = obtener_cliente(db, id)
    if not cliente:
        error_not_found('Cliente')
    return cliente

@router.put('/{id}', response_model=ClienteOut)
def api_actualizar_cliente(id: int, data: ClienteUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    cli = actualizar_cliente(db, id, data)
    if not cli:
        error_not_found('Cliente')
    return cli

@router.delete('/{id}')
def api_eliminar_cliente(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = eliminar_cliente(db, id)
    if not ok:
        error_not_found('Cliente')
    return {'mensaje': 'Cliente eliminado'}

