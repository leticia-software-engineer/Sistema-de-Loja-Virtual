from fastapi import APIRouter
from pydantic import BaseModel, Field
from Fonte.produto_fisico import ProdutoFisico
from enum import Enum

produto_routes = APIRouter(prefix= "/produtofisico", tags=["produtos"])

class freteEnum(str, Enum):
    sim = "sim"
    não = "não"

class produtofisico(BaseModel):
    nome: str
    cod: int = Field(..., gt=0)
    categoria:str
    preco: float = Field(..., gt=0)
    estoque: int = Field(...,gt=0)
    frete: freteEnum

@produto_routes.post("/cadastrodoprodutofisico/", response_model = None)
def cadastrar(produtof: produtofisico):

    produtofisico = ProdutoFisico(
        produtof.nome,
        produtof.cod,
        produtof.categoria,
        produtof.preco,
        produtof.estoque,
        produtof.frete
    )

    resposta = ProdutoFisico.cadastrar()
    return  {"mensagem": "Cliente cadastrado com sucesso!", "dados": resposta}

@produto_routes.post("/leituraprodutofisico/", response_model = None)
def ler(produtof: produtofisico):

    produtofisico = ProdutoFisico(
        produtof.nome,
        produtof.cod,
        produtof.categoria,
        produtof.preco,
        produtof.estoque,
        produtof.frete
    )

    resposta = ProdutoFisico.ler()
    return  {"mensagem": "Produto físico: ", "dados": resposta}