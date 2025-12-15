from Fonte.nota import NotaFiscal

def test_gerarnota():
    instancia = NotaFiscal(1)
    instancia.vernota()
    assert instancia
