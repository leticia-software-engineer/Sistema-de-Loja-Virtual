from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from Fonte.cliente import Cliente



cliente_routes = APIRouter(prefix="/cliente", tags=["autenticacao"])

class cliente(BaseModel):
    nome: str
    email: str
    cpf: str = Field(..., min_length=11, max_length=11)
    rua: str
    cep: str = Field(..., min_length=8, max_length=8)


@cliente_routes.post("/acessodocliente/cadastrar/", response_model=None)
def cadastrar(usuario: cliente):

    try:
        cliente = Cliente(
            usuario.nome,
            usuario.email,
            usuario.cpf,
            usuario.rua,
            usuario.cep
        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    resultado = cliente.cadastrar()  
    return {"dados": resultado}


@cliente_routes.post("/acessodocliente/ler/", response_model=None)
def ler(usuario: cliente):

    try:
        cliente = Cliente(
            usuario.nome,
            usuario.email,
            usuario.cpf,
            usuario.rua,
            usuario.cep
        )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    resposta = cliente.ler()  

    return {"dados": resposta}

@cliente_routes.post("/acessodocliente/atualizar/", response_model=None)
def atualizar(usuario: cliente):

    try:
        cliente = Cliente(
        usuario.nome,
        usuario.email,
        usuario.cpf,
        usuario.rua,
        usuario.cep
    )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))
    resposta = cliente.atualizar() 
    responda = cliente.ler() 

    return {"dados": responda}

@cliente_routes.post("/acessodocliente/deletar/", response_model=None)
def deletar(usuario: cliente):

    try:
        cliente = Cliente(
        usuario.nome,
        usuario.email,
        usuario.cpf,
        usuario.rua,
        usuario.cep
    )
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))

    resposta = cliente.deletar() 

    return {"dados": resposta}
