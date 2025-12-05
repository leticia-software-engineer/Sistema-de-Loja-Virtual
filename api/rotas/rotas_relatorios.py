from fastapi import APIRouter

relatorios_routes = APIRouter(prefix= "/relatorio", tags=["relatorio"])

@relatorios_routes.get("/")
async def sum(self):
    return {"mensagem" : "olá"}