from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.routers import login, clientes, polizas, pagos, siniestros, usuarios

app = FastAPI(title='Aseguradora API - Refactor')

origins = ['http://localhost:5173', 'http://localhost:3000', 'http://127.0.0.1:5173']


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # permite cualquier origen
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# Crear tablas
Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(clientes.router)
app.include_router(polizas.router)
app.include_router(pagos.router)
app.include_router(siniestros.router)
app.include_router(usuarios.router)

# Run: uvicorn app.main:app --reload
