from fastapi import APIRouter

auth_routes = APIRouter(prefix="/autenticacao", tags=["autenticacao"])

@auth_routes.get("/")
async def autenticar(self):
    return {"autenticacao": "rota de autenticação", "autenticado": False}