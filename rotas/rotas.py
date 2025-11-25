from fastapi import APIRouter

routes = APIRouter(prefix= "/ordens", tags=["ordens"])

@routes.get("/")
async def sum(self):
    return {"mensagem" : "olá"}