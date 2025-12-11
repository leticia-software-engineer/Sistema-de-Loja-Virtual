import pytest
from Fonte.carrinho import Carrinho


def test_adicionar_produto_valido_ao_carrinho():
    carrinho = Carrinho("64024926490", 1, 1, "sim")
    carrinho.adicionar_carrinho()
    assert carrinho


def test_visualizar_itens_do_carrinho():
    carrinho = Carrinho("64024926490", 1, 1, "sim")
    carrinho.visualizar_carrinho()
    assert carrinho


