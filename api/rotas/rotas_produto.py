from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from Fonte.produto_fisico import ProdutoFisico, LerProdutos
from enum import Enum
from Fonte.produto_digital import ProdutoDigital

produto_routes = APIRouter(prefix= "/produto", tags=["produtos"])

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


class leitura(BaseModel):
    cod: int = Field(..., gt=0)

@produto_routes.post("/cadastrarprodutofisico/", response_model = None)
def cadastrar(produtof: Produtofisico):
    try:
        produtofisico = ProdutoFisico(
            produtof.nome,
            produtof.cod,
            produtof.categoria,
            produtof.preco,
            produtof.estoque,
            produtof.frete
        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    resposta = produtofisico.cadastrar()
    return  {"dados": resposta}

@produto_routes.get("/leituratodososprodutos/", response_model = None)
def ler_tudo():

    resposta = ProdutoFisico.listar()
    return  {"dados": resposta}

@produto_routes.post("/buscaprodutos/", response_model = None)
def ler(produtof: leitura):

    try:
        produtof = LerProdutos(
            produtof.cod
        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))
    resposta = produtof.ler()
    return  {"dados": resposta}



@produto_routes.post("/atualizarprodutofisico/", response_model = None)
def atualizar(produtof: Produtofisico):

    try:
        produtofisico = ProdutoFisico(
        produtof.nome,
        produtof.cod,
        produtof.categoria,
        produtof.preco,
        produtof.estoque,
        produtof.frete
    )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    resposta = produtofisico.atualizar()
    produto_atual = produtofisico.ler()
    return  {"dados": produto_atual}

@produto_routes.post("/deletarprodutofisico/", response_model = None)
def deletar(produtof: Produtofisico):

    try:
        produtofisico = ProdutoFisico(
        produtof.nome,
        produtof.cod,
        produtof.categoria,
        produtof.preco,
        produtof.estoque,
        produtof.frete
    )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    resposta = produtofisico.deletar()
    return  {"dados": resposta}



class produtodigital(BaseModel):
    nome: str
    cod: int = Field(..., gt=0)
    categoria:str
    preco: float = Field(..., gt=0)
    estoque: int = Field(...,gt=0)

@produto_routes.post("/cadastrarprodutodigital/", response_model = None)
def cadastrar(produtod: produtodigital):

    try:
        produtodigital = ProdutoDigital(
        produtod.nome,
        produtod.cod,
        produtod.categoria,
        produtod.preco,
        produtod.estoque )

    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))
    resposta = produtodigital.cadastrar()
    return  {"dados": resposta}



@produto_routes.post("/atualizarprodutodigital/", response_model = None)
def atualizar(produtod: produtodigital):

    try:
        produtodigital = ProdutoDigital(
        produtod.nome,
        produtod.cod,
        produtod.categoria,
        produtod.preco,
        produtod.estoque )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    resposta = produtodigital.atualizar()
    produto_atual = produtodigital.ler()
    return  {"dados": produto_atual}

@produto_routes.post("/deletarprodutodigital/", response_model = None)
def deletar(produtod: produtodigital):

    try:
        produtodigital = ProdutoDigital(
        produtod.nome,
        produtod.cod,
        produtod.categoria,
        produtod.preco,
        produtod.estoque )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    resposta = produtodigital.deletar()
    return  {"dados": resposta}

