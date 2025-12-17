from fastapi import FastAPI

app = FastAPI()

from api.rotas.rotas_cliente import cliente_routes
from api.rotas.rotas_produto import produto_routes
from api.rotas.rotascarrinho import carrinho_routes
from api.rotas.rotas_pedido import pedido_routes
from api.rotas.rotas_pagamento import pagamento_routes
from api.rotas.rotas_frete import frete_routes
from api.rotas.rotas_relatorios import relatorios_routes
from api.rotas.rotasconfig import configuracoes_routes

app.include_router(cliente_routes)
app.include_router(produto_routes)
app.include_router(carrinho_routes)
app.include_router(pedido_routes)
app.include_router(pagamento_routes)
app.include_router(frete_routes)
app.include_router(relatorios_routes)
app.include_router(configuracoes_routes)

#para rodar executar no terminal uvicorn main:app --reload