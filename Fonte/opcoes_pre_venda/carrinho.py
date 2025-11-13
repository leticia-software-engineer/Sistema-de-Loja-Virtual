'''
A classe carrinho é responsável por salvar os produtos escolhidos pelo cliente em uma parte específica da memória onde serão acessados no momento da veda
a partir dessa classe é possível ter um controle da quantidade de itens que o cliente pretende comprar e reunir diversos produtos na mesma compra.
Além disso, é possível remover do carrinho aqueles produtos que o cliente desejar.
'''

from Fonte.opcoes_pre_venda.produto import Produto
class Carrinho():

    def __init__(self, quantidade):
        self.quantidade = quantidade
        self.produto = Produto()
        pass

    def adicionar(self):
        pass

    def remover(self):
        pass

    def alterar_quant(self):
        pass
