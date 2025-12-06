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

def test_cadastrar_produto_digital_invalido():
    produto_invalido = ProdutoDigital("Ebook O ovo", 0, "livros", 0, 100)
    produto_invalido.cadastrar()
    assert produto_invalido

def test_ler_produto_digital_com_codigo_invalido():
    produto_invalido = ProdutoDigital("Ebook O Pequeno Principe", 111, "livros", 50, 100)
    produto_invalido.ler()
    assert produto_invalido

def test_atualizar_dado_produto_invalido():
    produto_inexistente = ProdutoDigital("Ebook O ovo", 0, "livros", 0, 100)
    produto_inexistente.atualizar()
    assert produto_inexistente

def test_deletar_produto_inexistente():
    produto_inexistente = ProdutoDigital("Ebook O ovo", 0, "livros", 0, 100)
    produto_inexistente.deletar()
    assert produto_inexistente
