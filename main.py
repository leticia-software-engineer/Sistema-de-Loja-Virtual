from fastapi import FastAPI

app = FastAPI()

from api.rotas.rotas_aut import auth_routes
from api.rotas.rotas import routes

app.include_router(auth_routes)
app.include_router(routes)

#para rodar executar no terminal uvicorn main:app --reload