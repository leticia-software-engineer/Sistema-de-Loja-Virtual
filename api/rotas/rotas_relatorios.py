from fastapi import APIRouter
from Fonte.relatorio import Relatorio

relatorios_routes = APIRouter(prefix= "/relatorio", tags=["relatorio"])


@relatorios_routes.get("/relatoriofaturamento")
def relatoriofaturamento():

    relatorio = Relatorio()

    resposta = relatorio.faturamento_periodo()
    return resposta


@relatorios_routes.get("/relatoriopedidosporcep")
def relatoriocep():

    relatorio = Relatorio()

    resposta = relatorio.pedidos_por_cep()
    return resposta


@relatorios_routes.get("/relatoriopedidosporstatus")
def relatorioporstatus():

    relatorio = Relatorio()

    resposta = relatorio.pedidos_por_status()
    return resposta

