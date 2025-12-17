from fastapi import APIRouter
from Fonte.configuracoes import Configuracoes

configuracoes_routes = APIRouter(prefix= "/configuracoes", tags=["configuracoes"])


@configuracoes_routes.get("/tabelafrete")
def tabelafrete():

    configuracoes = Configuracoes()

    resposta = configuracoes.tabela_frete()
    return f"{resposta}"


@configuracoes_routes.get("/cancelamentopolitica")
def cancelamentoorientacoes():

    configuracoes = Configuracoes()

    resposta = configuracoes.politica_de_cancelamento()
    return resposta


@configuracoes_routes.get("/orientacoes")
def orientacoesdeuso():

    configuracoes = Configuracoes()

    resposta = configuracoes.orientacoes_da_aplicacao()
    return resposta

