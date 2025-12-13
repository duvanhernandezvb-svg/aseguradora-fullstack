from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.models.poliza import Poliza
from app.schemas import PolizaCreate, PolizaUpdate
from app.crud.cliente import obtener_cliente

def crear_poliza(db: Session, data: PolizaCreate):
    # Validar cliente existente
    cliente = obtener_cliente(db, data.cliente_id)
    if not cliente:
        raise HTTPException(status_code=400, detail=f"Cliente con id {data.cliente_id} no existe")

    # Validar número de póliza duplicado
    existente = db.query(Poliza).filter(Poliza.numero_poliza == data.numero_poliza).first()
    if existente:
        raise HTTPException(status_code=400, detail="Número de póliza ya existe")

    # Validar fechas
    if data.fecha_fin < data.fecha_inicio:
        raise HTTPException(status_code=400, detail="fecha_fin no puede ser menor que fecha_inicio")

    # Crear póliza
    try:
        poliza = Poliza(**data.dict())
        db.add(poliza)
        db.commit()
        db.refresh(poliza)
        return poliza
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error de integridad en la base de datos: {e.orig}")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear póliza: {str(e)}")


def obtener_poliza(db: Session, id: int):
    return db.query(Poliza).filter(Poliza.id == id).first()


def obtener_todas(db: Session):
    return db.query(Poliza).all()


def actualizar_poliza(db: Session, id: int, data: PolizaUpdate):
    poliza = obtener_poliza(db, id)
    if not poliza:
        return None
    for k, v in data.dict(exclude_unset=True).items():
        setattr(poliza, k, v)
    db.commit()
    db.refresh(poliza)
    return poliza


def eliminar_poliza(db: Session, id: int):
    poliza = obtener_poliza(db, id)
    if not poliza:
        return False
    db.delete(poliza)
    db.commit()
    return True
