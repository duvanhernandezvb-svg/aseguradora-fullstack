from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UsuarioCreate, UsuarioUpdate, UsuarioOut
from app.crud.usuario import (
    crear_usuario,
    obtener_usuario,
    obtener_todos_usuarios,
    actualizar_usuario,
    eliminar_usuario
)
from app.auth import get_current_user
from app.errors import error_not_found

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioOut)
def api_crear_usuario(data: UsuarioCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crear_usuario(db, data)

@router.get("/", response_model=list[UsuarioOut])
def api_listar_usuarios(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return obtener_todos_usuarios(db)

@router.get("/{id}", response_model=UsuarioOut)
def api_obtener_usuario(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    usuario = obtener_usuario(db, id)
    if not usuario:
        error_not_found("Usuario")
    return usuario

@router.put("/{id}", response_model=UsuarioOut)
def api_actualizar_usuario(id: int, data: UsuarioUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    user_updated = actualizar_usuario(db, id, data)
    if not user_updated:
        error_not_found("Usuario")
    return user_updated

@router.delete("/{id}")
def api_eliminar_usuario(id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = eliminar_usuario(db, id)
    if not ok:
        error_not_found("Usuario")
    return {"mensaje": "Usuario eliminado"}
