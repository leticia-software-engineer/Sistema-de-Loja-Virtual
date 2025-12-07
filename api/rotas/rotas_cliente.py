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

    cliente = Cliente(
        usuario.nome,
        usuario.email,
        usuario.cpf,
        usuario.rua,
        usuario.cep
    )

    resultado = cliente.cadastrar()  
    return {"dados": resultado}


@cliente_routes.post("/acessodocliente/ler/", response_model=None)
def ler(usuario: cliente):

    cliente = Cliente(
        usuario.nome,
        usuario.email,
        usuario.cpf,
        usuario.rua,
        usuario.cep
    )

    resposta = cliente.ler()  

    return {"dados": resposta}

@cliente_routes.post("/acessodocliente/atualizar/", response_model=None)
def atualizar(usuario: cliente):

    cliente = Cliente(
        usuario.nome,
        usuario.email,
        usuario.cpf,
        usuario.rua,
        usuario.cep
    )

    resposta = cliente.atualizar() 
    responda = cliente.ler() 

    return {"dados": responda}

@cliente_routes.post("/acessodocliente/deletar/", response_model=None)
def deletar(usuario: cliente):

    cliente = Cliente(
        usuario.nome,
        usuario.email,
        usuario.cpf,
        usuario.rua,
        usuario.cep
    )

    resposta = cliente.deletar() 

    return {"dados": resposta}
