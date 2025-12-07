import pytest
from Fonte.carrinho import Carrinho

def test_adicionar_produto_valido_ao_carrinho():
    carrinho = Carrinho("11012667324", 10, 1, "não")
    carrinho.adicionar_carrinho()
    assert carrinho

def test_visualizar_itens_do_carrinho():
    carrinho = Carrinho()
    carrinho.visualizar_carrinho()
    assert carrinho

def test_apagar_carrinho():
    carrinho = Carrinho()
    carrinho.excluir_item_carrinho(10)
    assert carrinho