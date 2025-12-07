from fastapi import APIRouter
from pydantic import BaseModel, Field
from Fonte.pedido import Pedido

pedido_routes = APIRouter(prefix="/pedido", tags=["pedido"])
class pedidos(BaseModel):
     confirmar: str 
     cpf: str = Field(..., min_length=11, max_length=11)
     confirma_cep: str = Field(..., min_length=8, max_length=8)
    
@pedido_routes.post("/calculodosubtotal", response_model=None)
def calcular(pedidox: pedidos):

    pedidoacalcular = Pedido(
        pedidox.confirmar,
        pedidox.cpf,
        pedidox.confirma_cep )

    resposta = pedidoacalcular.calcular_subtotal()
    return  {"dados": resposta}

@pedido_routes.post("/calculodosubtotalpedidoscomfrete", response_model=None)
def calcular(pedidox: pedidos):

    pedidoacalcular = Pedido(
        pedidox.confirmar,
        pedidox.cpf,
        pedidox.confirma_cep )

    resposta = pedidoacalcular.calcular_subtotal_com_frete()
    return  {"dados": resposta}


@pedido_routes.post("/fecharpedido", response_model=None)
def fechar(pedidox: pedidos):

    pedidoafechar = Pedido(
        pedidox.confirmar,
        pedidox.cpf,
        pedidox.confirma_cep )

    resposta1 = pedidoafechar.calcular_subtotal()
    resposta = pedidoafechar.fechar_pedido()
    return  {"dados": resposta}


@pedido_routes.post("/verpedidos", response_model=None)

def ver(pedidox: pedidos):

    pedidover = Pedido(
        pedidox.confirmar,
        pedidox.cpf,
        pedidox.confirma_cep )

    resposta = pedidover.visualizar_meus_pedidos()
    return  {"dados": resposta}

