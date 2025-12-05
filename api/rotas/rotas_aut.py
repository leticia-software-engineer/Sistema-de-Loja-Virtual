from fastapi import APIRouter

cliente_routes = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@cliente_routes.get("/")
async def autenticar(self):
    return {"autenticacao": "rota de autenticação", "autenticado": False}