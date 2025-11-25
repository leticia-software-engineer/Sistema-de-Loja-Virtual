'''A classe Pedido armazena todos os dados da compra e a partir das informações gera um cupom da venda, além disso ela é responsável por permitir 
o cancelamento de um pedido seguindo as políticas de cancelamento informadas nas configurações.'''
import json
from cliente import Cliente
from carrinho import Carrinho
from frete import Frete
from cupom import CupomDesconto
from expedicao import Expedicao

class Pedido():
    def __init__(self, total, status, carrinho: Carrinho, cliente: Cliente, frete: Frete, desconto: CupomDesconto, expedicao: Expedicao):
        self.carrinho = carrinho
        self.total = total
        self.status = status
        self.cliente = cliente
        self.frete = frete
        self.desconto = desconto
        self.expedicao = expedicao

        
        
    def cancelar(self):
        pass
    def gerar_nota(self):
        nota = []

        pass
    def subtotal(self):
        pass