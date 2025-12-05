from fastapi import APIRouter

produto_routes = APIRouter(prefix= "/produtos", tags=["produtos"])

@produto_routes.get("/")
async def sum(self):
    return {"mensagem" : "olá"}