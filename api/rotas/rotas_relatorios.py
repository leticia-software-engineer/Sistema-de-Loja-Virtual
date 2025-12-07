from fastapi import APIRouter
from Fonte.relatorio import Relatorio

relatorios_routes = APIRouter(prefix= "/relatorio", tags=["relatorio"])


@relatorios_routes.post("/relatoriofaturamento")
def relatoriofaturamento():

    relatorio = Relatorio()

    resposta = relatorio.faturamento_periodo()
    return resposta


@relatorios_routes.post("/relatoriopedidosporcep")
def relatoriocep():

    relatorio = Relatorio()

    resposta = relatorio.pedidos_por_cep()
    return resposta


@relatorios_routes.post("/relatoriopedidosporstatus")
def relatorioporstatus():

    relatorio = Relatorio()

    resposta = relatorio.pedidos_por_status()
    return resposta

