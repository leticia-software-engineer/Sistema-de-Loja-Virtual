import pytest
from carrinho import Carrinho

def test_adicionar_produto_valido_ao_carrinho():
    carrinho = Carrinho()
    carrinho.adicionar_carrinho("Ebook Pequeno Príncipe", 10, 1, "não")
    assert carrinho

def test_visualizar_itens_do_carrinho():
    carrinho = Carrinho()
    carrinho.visualizar_carrinho()
    assert carrinho

def test_apagar_carrinho():
    carrinho = Carrinho()
    carrinho.excluir_item_carrinho(10)
    assert carrinho