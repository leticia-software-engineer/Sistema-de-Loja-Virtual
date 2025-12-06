from fastapi import FastAPI

app = FastAPI()

from api.rotas.rotas_cliente import cliente_routes
from api.rotas.rotas_adm_produto import produto_routes

app.include_router(cliente_routes)
app.include_router(produto_routes)

#para rodar executar no terminal uvicorn main:app --reload