from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import crear_token, autenticar_usuario
from pydantic import BaseModel

router = APIRouter(tags=["auth"])


class LoginSchema(BaseModel):
    username: str
    password: str


@router.post("/login", status_code=status.HTTP_200_OK)
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = autenticar_usuario(db, data.username, data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña inválidos"
        )

    token = crear_token({"sub": user.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }



