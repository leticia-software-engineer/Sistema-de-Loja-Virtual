from Fonte.pagamentos import Pagamento

def test_pagar():
    instancia = Pagamento(1, "pix", 35.5, "pago parcialmente")
    instancia.registrar_pagamento()
    assert instancia
