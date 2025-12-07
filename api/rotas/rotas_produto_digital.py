from fastapi import APIRouter
from pydantic import BaseModel, Field
from Fonte.produto_digital import ProdutoDigital


produtodigital_routes = APIRouter(prefix="/produtodigital", tags=["produtodigital"])

class produtodigital(BaseModel):
    nome: str
    cod: int = Field(..., gt=0)
    categoria:str
    preco: float = Field(..., gt=0)
    estoque: int = Field(...,gt=0)

@produtodigital_routes.post("/cadastrarprodutodigital/", response_model = None)
def cadastrar(produtod: produtodigital):

    produtodigital = ProdutoDigital(
        produtod.nome,
        produtod.cod,
        produtod.categoria,
        produtod.preco,
        produtod.estoque )

    resposta = produtodigital.cadastrar()
    return  {"dados": resposta}

@produtodigital_routes.post("/leituraprodutodigital/", response_model = None)
def ler(produtod: produtodigital):

    produtodigital = ProdutoDigital(
        produtod.nome,
        produtod.cod,
        produtod.categoria,
        produtod.preco,
        produtod.estoque)

    resposta = produtodigital.ler()
    return  {"dados": resposta}

@produtodigital_routes.post("/atualizarprodutodigital/", response_model = None)
def atualizar(produtod: produtodigital):

    produtodigital = ProdutoDigital(
        produtod.nome,
        produtod.cod,
        produtod.categoria,
        produtod.preco,
        produtod.estoque )

    resposta = produtodigital.atualizar()
    produto_atual = produtodigital.ler()
    return  {"dados": produto_atual}

@produtodigital_routes.post("/deletarprodutodigital/", response_model = None)
def deletar(produtod: produtodigital):

    produtodigital = ProdutoDigital(
        produtod.nome,
        produtod.cod,
        produtod.categoria,
        produtod.preco,
        produtod.estoque )

    resposta = produtodigital.deletar()
    return  {"dados": resposta}

