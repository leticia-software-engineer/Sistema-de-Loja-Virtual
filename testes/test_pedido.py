from Fonte.pedido import Pedido
import pytest

def test_calculo_de_subtotal_pedido():
    instancia = Pedido("sim", "11012667324", "63210000")
    instancia.calcular_subtotal()
    assert instancia

def test_fechar_pedido():
    instancia = Pedido("sim", "11012667324", "63210000")
    instancia.fechar_pedido()
    assert instancia

def test_visualizar_pedidos_feitos():
    instancia = Pedido("sim", "11012667324", "63210000")
    instancia.visualizar_meus_pedidos()
    assert instancia

def test_calculo_de_subtotal_pedido_frete():
    instancia = Pedido("sim", "11012667324", "63210000")
    instancia.calcular_subtotal_com_frete()
    assert instancia
