from fastapi import APIRouter
from pydantic import BaseModel, Field
from Fonte.carrinho import Carrinho
from enum import Enum

carrinho_routes = APIRouter(prefix="/carrinho", tags= ["carrinho"])

class freteEnum(str, Enum):
    sim = "sim"
    não = "não"
class carrinho(BaseModel):
    
    cpf: str = Field(..., min_length=11, max_length=11)
    codigo_produto: int = Field(..., gt=0)
    quantidade: int = Field(..., gt=0)
    com_frete: freteEnum

@carrinho_routes.post("/adicionaraocarrinho/", response_model=None)
def adicionaraocarrinho(carrinhocriar: carrinho):
    carrinho = Carrinho(
        carrinhocriar.cpf,
        carrinhocriar.codigo_produto,
        carrinhocriar.quantidade,
        carrinhocriar.com_frete
    )
    resposta = carrinho.adicionar_carrinho()
    return{"retorno": resposta}

@carrinho_routes.post("/visualizarseitememcarrinho/", response_model=None)
def visualizarcarrinho(carrinhov: carrinho):
    carrinho = Carrinho(
        carrinhov.cpf,
        carrinhov.codigo_produto,
        carrinhov.quantidade,
        carrinhov.com_frete
    )
    resposta = carrinho.visualizar_carrinho()
    return{"retorno": resposta}

@carrinho_routes.post("/excluiritememcarrinho/", response_model=None)
def excluircarrinho(carrinhod: carrinho):
    carrinho = Carrinho(
        carrinhod.cpf,
        carrinhod.codigo_produto,
        carrinhod.quantidade,
        carrinhod.com_frete
    )
    resposta = carrinho.excluir_item_carrinho()
    mostrar = carrinho.visualizar_carrinho()
    return{"retorno": resposta, "dados": mostrar}

