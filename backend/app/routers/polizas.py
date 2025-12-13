from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import PolizaCreate, PolizaUpdate, PolizaOut
from app.crud.poliza import crear_poliza, obtener_poliza, obtener_todas, actualizar_poliza, eliminar_poliza
from app.auth import get_current_user
from fastapi import HTTPException

router = APIRouter(prefix='/polizas', tags=['Polizas'])


@router.post('/', response_model=PolizaOut)
def api_crear_poliza(data: PolizaCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crear_poliza(db, data)


@router.get('/', response_model=list[PolizaOut])
def api_listar_polizas(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return obtener_todas(db)


@router.get('/{id}', response_model=PolizaOut)
def api_obtener_poliza(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    poliza = obtener_poliza(db, id)
    if not poliza:
        raise HTTPException(status_code=404, detail="Póliza no encontrada")
    return poliza


@router.put('/{id}', response_model=PolizaOut)
def api_actualizar_poliza(id: int, data: PolizaUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    p = actualizar_poliza(db, id, data)
    if not p:
        raise HTTPException(status_code=404, detail="Póliza no encontrada")
    return p


@router.delete('/{id}')
def api_eliminar_poliza(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = eliminar_poliza(db, id)
    if not ok:
        raise HTTPException(status_code=404, detail="Póliza no encontrada")
    return {'mensaje': 'Póliza eliminada'}
