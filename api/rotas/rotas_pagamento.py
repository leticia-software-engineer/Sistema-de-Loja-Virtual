from fastapi import APIRouter
from pydantic import BaseModel, Field
from Fonte.pagamentos import Pagamento
from enum import Enum

pagamento_routes = APIRouter(prefix="/pagamento", tags=["pagamento"])

class confirmarEnum(str, Enum):
    sim = "sim"
    não = "não"
class pagamento(BaseModel):
    num_pedido: int
    forma_pagamento: str = Field(..., min_length=3, max_length=20)
    valor_pago: float = Field(..., gt=0)
    status: str
    
@pagamento_routes.post("/registrodopagamento", response_model=None)
def calcular(pag: pagamento):

    pedidoapagar = Pagamento(
        pag.num_pedido,
        pag.forma_pagamento,
        pag.valor_pago,
        pag.status)
    
    resposta1 = pedidoapagar.atualizar_estoque()
    resposta = pedidoapagar.registrar_pagamento()
    return  {"dados": resposta}