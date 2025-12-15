from Fonte.frete import Frete

def test_ver_frete():
    instancia = Frete("63260000")
    instancia.verificar_valor_frete()
    assert instancia