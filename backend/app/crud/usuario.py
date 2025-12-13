from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas import UsuarioCreate, UsuarioUpdate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_usuario(db: Session, usuario: UsuarioCreate):
    hashed_password = pwd_context.hash(usuario.password)
    db_usuario = Usuario(username=usuario.username, hashed_password=hashed_password, is_active=usuario.is_active)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def obtener_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def obtener_usuario_por_username(db: Session, username: str):
    return db.query(Usuario).filter(Usuario.username == username).first()

def obtener_todos_usuarios(db: Session):
    return db.query(Usuario).all()

def actualizar_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        if usuario.password:
            db_usuario.hashed_password = pwd_context.hash(usuario.password)
        if usuario.is_active is not None:
            db_usuario.is_active = usuario.is_active
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def eliminar_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        return True
    return False

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica si la contraseña coincide con el hash bcrypt.
    Retorna False si el hash es inválido o no coincide.
    """
    if not hashed_password:
        return False
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except ValueError:
        # Captura errores si el hash no es válido
        return False

