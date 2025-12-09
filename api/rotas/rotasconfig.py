from fastapi import APIRouter
from Fonte.configuracoes import Configuracoes

configuracoes_routes = APIRouter(prefix= "/configuracoes", tags=["configuracoes"])


@configuracoes_routes.post("/tabelafrete")
def tabelafrete():

    configuracoes = Configuracoes()

    resposta = configuracoes.tabela_frete()
    return f"{resposta}"


@configuracoes_routes.post("/cancelamentopolitica")
def cancelamentoorientacoes():

    configuracoes = Configuracoes()

    resposta = configuracoes.politica_de_cancelamento()
    return resposta


@configuracoes_routes.post("/orientacoes")
def orientacoesdeuso():

    configuracoes = Configuracoes()

    resposta = configuracoes.orientacoes_da_aplicacao()
    return resposta

