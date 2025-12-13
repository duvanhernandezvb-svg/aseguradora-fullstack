from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import crear_token, autenticar_usuario
from pydantic import BaseModel

router = APIRouter(tags=["auth"])

# Modelo para recibir los datos en JSON
class LoginSchema(BaseModel):
    username: str
    password: str

@router.post('/login')
def login(data: LoginSchema, db: Session = Depends(get_db)):
    try:
        user = autenticar_usuario(db, data.username, data.password)
        if not user:
            raise HTTPException(status_code=401, detail='Usuario o contraseña inválidos')

        token = crear_token({'sub': user.username})
        return {"access_token": token, "token_type": "bearer"}

    except HTTPException:
        # Propagar errores controlados
        raise
    except Exception as e:
        # Captura cualquier error inesperado y retorna un mensaje legible
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


