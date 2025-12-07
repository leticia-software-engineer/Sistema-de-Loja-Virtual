from fastapi import APIRouter
from pydantic import BaseModel, Field
from Fonte.produto_fisico import ProdutoFisico
from enum import Enum

produtofisico_routes = APIRouter(prefix= "/produtofisico", tags=["produtos"])

class freteEnum(str, Enum):
    sim = "sim"
    não = "não"

class Produtofisico(BaseModel):
    nome: str
    cod: int = Field(..., gt=0)
    categoria:str
    preco: float = Field(..., gt=0)
    estoque: int = Field(...,gt=0)
    frete: freteEnum

@produtofisico_routes.post("/cadastrarprodutofisico/", response_model = None)
def cadastrar(produtof: Produtofisico):

    produtofisico = ProdutoFisico(
        produtof.nome,
        produtof.cod,
        produtof.categoria,
        produtof.preco,
        produtof.estoque,
        produtof.frete
    )

    resposta = produtofisico.cadastrar()
    return  {"dados": resposta}

@produtofisico_routes.post("/leituraprodutofisico/", response_model = None)
def ler(produtof: Produtofisico):

    produtofisico = ProdutoFisico(
        produtof.nome,
        produtof.cod,
        produtof.categoria,
        produtof.preco,
        produtof.estoque,
        produtof.frete
    )

    resposta = produtofisico.ler()
    return  {"dados": resposta}

@produtofisico_routes.post("/atualizarprodutofisico/", response_model = None)
def atualizar(produtof: Produtofisico):

    produtofisico = ProdutoFisico(
        produtof.nome,
        produtof.cod,
        produtof.categoria,
        produtof.preco,
        produtof.estoque,
        produtof.frete
    )

    resposta = produtofisico.atualizar()
    produto_atual = produtofisico.ler()
    return  {"dados": produto_atual}

@produtofisico_routes.post("/deletarprodutofisico/", response_model = None)
def deletar(produtof: Produtofisico):

    produtofisico = ProdutoFisico(
        produtof.nome,
        produtof.cod,
        produtof.categoria,
        produtof.preco,
        produtof.estoque,
        produtof.frete
    )

    resposta = produtofisico.deletar()
    return  {"dados": resposta}

