from fastapi import APIRouter
from pydantic import BaseModel, Field
from Fonte.pedido import Pedido
from Fonte.cancelamento_pedido import CancelarPedido
from Fonte.nota import NotaFiscal

pedido_routes = APIRouter(prefix="/pedido", tags=["pedido"])
class pedidos(BaseModel):
     confirmar: str 
     cpf: str = Field(..., min_length=11, max_length=11)
     confirma_cep: str = Field(..., min_length=8, max_length=8)

class fechar_pedidos(BaseModel):
     confirmar: str 
     confirme_cpf: str = Field(..., min_length=11, max_length=11)
     confirma_cep: str = Field(..., min_length=8, max_length=8)

class cancelarpedidos(BaseModel):
    
     confirmar: str 
     cpf: str = Field(..., min_length=11, max_length=11)
     confirma_cep: str = Field(..., min_length=8, max_length=8)
     num_pedido: int

class mostrarnota(BaseModel):
    num_pedido: int = Field(..., gt=0)


@pedido_routes.post("/calculodosubtotalpedidoscomfrete", response_model=None)
def calcular(pedidox: pedidos):

    pedidoacalcular = Pedido(
        pedidox.confirmar,
        pedidox.cpf,
        pedidox.confirma_cep )

    resposta = pedidoacalcular.calcular_subtotal_com_frete()
    return  {"dados": resposta}


@pedido_routes.post("/fecharpedido", response_model=None)
def fechar(pedidox: fechar_pedidos):

    pedidoafechar = Pedido(
        pedidox.confirmar,
        pedidox.confirme_cpf,
        pedidox.confirma_cep )

    resposta1 = pedidoafechar.calcular_subtotal()
    resposta = pedidoafechar.fechar_pedido()
    return  {"dados": resposta}

@pedido_routes.post("/fecharpedidocomfrete", response_model=None)
def fechar(pedidox: fechar_pedidos):

    pedidoafechar = Pedido(
        pedidox.confirmar,
        pedidox.confirme_cpf,
        pedidox.confirma_cep )

    resposta1 = pedidoafechar.calcular_subtotal_com_frete()
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

@pedido_routes.post("/cancelarpedidos", response_model=None)

def cancelarpedido(pedidox: cancelarpedidos):

    pedidocancelar = CancelarPedido(
        pedidox.confirmar,
        pedidox.cpf,
        pedidox.confirma_cep,
        pedidox.num_pedido )

    resposta = pedidocancelar.cancelar()
    return  {"dados": resposta}

@pedido_routes.post("/vernota/", response_model= None)

def veranota(nota: mostrarnota):
    nota = NotaFiscal(
        nota.num_pedido
    )
    resposta = nota.vernota()
    return {"Dados ": resposta}