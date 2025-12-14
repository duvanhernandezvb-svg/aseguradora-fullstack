from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.config import JWT_SECRET, JWT_ALGORITHM, JWT_EXPIRATION_MINUTES
from app.crud.usuario import obtener_usuario_por_username, verify_password
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def crear_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET, algorithm=JWT_ALGORITHM)

def autenticar_usuario(db: Session, username: str, password: str):
    print(">>> AUTENTICAR_USUARIO <<<")
    print("Username recibido:", username)

    user = obtener_usuario_por_username(db, username)
    print("Usuario encontrado:", user)

    if not user:
        print("❌ Usuario NO encontrado")
        return None

    print("Hash en BD:", user.hashed_password)
    print("Password recibido:", password)

    result = verify_password(password, user.hashed_password)
    print("Resultado verify_password:", result)

    if not result:
        print("❌ Password NO válido")
        return None

    print("✅ Autenticación exitosa")
    return user


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido o expirado")

    user = obtener_usuario_por_username(db, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return user
