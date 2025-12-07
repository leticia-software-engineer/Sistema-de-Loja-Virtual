from fastapi import APIRouter
from pydantic import BaseModel, Field
from Fonte.frete import Frete
from Fonte.expedicao import Expedicao

frete_routes = APIRouter(prefix= "/fretes", tags=["frete"])

class frete(BaseModel):
    cep: str = Field(..., min_length=8, max_length=8)

@frete_routes.post("/verfreteparameucep")
def verfrete(frete: frete):
    freteinstancia = Frete(
        frete.cep
    )

    resposta = freteinstancia.verificar_valor_frete()
    return{"dados": resposta}

class expedicao(BaseModel):
    codigo_de_entrega: str 

@frete_routes.post("/marcarenvio")
def marcarenvio(marcar: expedicao):
    envioinstancia = Expedicao(
        marcar.codigo_de_entrega
    )

    resposta = envioinstancia.marcar_envio()
    return{"dados": resposta}


    