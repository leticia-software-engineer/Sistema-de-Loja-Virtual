from fastapi import APIRouter

menu_routes = APIRouter(prefix= "/menu", tags=["menu"])

@menu_routes.get("/")
async def sum(self):
    return {"mensagem" : "olá"}