import pytest
from Fonte.produto_digital import ProdutoDigital

def test_verificar_cadastro_de_produto_digital_valido():
    produto_valido = ProdutoDigital("Ebook O Pequeno Principe", 3, "livros", 20, 20)
    produto_valido.cadastrar()
    assert produto_valido

def test_verificar_leitura_de_produto_digital():
    produto_valido = ProdutoDigital("Ebook O Pequeno Principe", 3, "livros", 20, 20)
    produto_valido.ler()
    assert produto_valido

def test_atualizar_produto_digital():
    produto_valido = ProdutoDigital("Ebook O Pequeno Principe", 3, "livros", 50, 100)
    produto_valido.atualizar()
    assert produto_valido

def test_excluir_produto_digital():
    produto_valido = ProdutoDigital("Ebook O Pequeno Principe", 3, "livros", 50, 100)
    produto_valido.deletar()
    assert produto_valido
