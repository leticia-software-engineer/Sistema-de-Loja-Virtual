from Fonte.cliente import Cliente
import pytest

def test_cadastro_de_cliente():
    crud = Cliente("Leticia", "euleticia@gmail.com", "12312312312", "Rua Maria", "63260000")
    crud.cadastrar()
    assert crud

def test_visualizacao_de_dados_cliente():
    crud = Cliente("Leticia", "euleticia@gmail.com", "12312312312", "Rua Maria", "63260000")
    crud.ler()
    assert crud

def test_atualizacao_dados_do_cliente():
    crud = Cliente("Leticia", "euleticiadias@gmail.com", "12312312312", "Rua Maria", "63210000")
    crud.atualizar()
    assert crud

def test_deletar_conta_cliente():
    crud = Cliente("Leticia", "euleticiadias@gmail.com", "12312312312", "Rua Maria", "63210000")
    crud.deletar()
    assert crud

