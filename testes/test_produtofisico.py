import pytest
from Fonte.produto_fisico import ProdutoFisico

def test_verificar_cadastro_de_produto_fisico_valido():
    produto_valido = ProdutoFisico("Vaso", 19, "utensilios", 20, 20)
    produto_valido.cadastrar()
    assert produto_valido

def test_verificar_leitura_de_produto_fisico():
    produto_valido = ProdutoFisico("Vaso", 19, "utensilios", 20, 20)
    produto_valido.ler()
    assert produto_valido

def test_atualizar_produto_fisico():
    produto_valido = ProdutoFisico("Vaso", 19, "utensilios", 50, 100)
    produto_valido.atualizar()
    assert produto_valido

def test_excluir_produto_fisico():
    produto_valido = ProdutoFisico("Vaso", 19, "utensilios", 50, 100)
    produto_valido.deletar()
    assert produto_valido
