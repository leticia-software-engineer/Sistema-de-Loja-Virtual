import pytest
from produto import Produto

def test_verificar_cadastro_de_produtos():
    produto_valido = Produto("árvore de natal", 60, "decoracao", 100, 20)
    produto_valido.cadastrar()

    assert produto_valido