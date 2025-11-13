'''A classe Pedido armazena todos os dados da compra e a partir das informações gera um cupom da venda, além disso ela é responsável por permitir 
o cancelamento de um pedido seguindo as políticas de cancelamento informadas nas configurações.'''

from Fonte.atores_do_sistema.cliente import Cliente
from Fonte.opcoes_pre_venda.carrinho import Carrinho
from frete import Frete
from Fonte.opcoes_pre_venda.cupom import CupomDesconto
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
        pass