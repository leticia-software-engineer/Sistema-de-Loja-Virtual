import pytest
from Fonte.itemcarrinho import Carrinho

def test_adicionar_ao_carrinho():
    carrinho = Carrinho()
    carrinho.adicionar("maca", 12)
    assert carrinho
