from fastapi import HTTPException, status

def error_unauthorized():
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No autorizado")

def error_not_found(entity: str):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{entity} no encontrado")

def error_already_exists(entity: str):
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"{entity} ya existe")
