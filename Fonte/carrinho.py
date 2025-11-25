'''
A classe ItemCarrinho é responsável por salvar os produtos escolhidos pelo cliente em uma parte específica da memória onde serão acessados no
momento da venda a partir dessa classe é possível ter um controle da quantidade de itens que o cliente pretende comprar e reunir diversos produtos
na mesma compra. Além disso, com a classe Carrinho é possível remover do carrinho ou alterar a quantidade daqueles produtos que o cliente desejar.
'''
from produto import Produto

class ItemCarrinho(Produto):
    def __init__(self, nome, cod, categoria, preco_unitario, estoque, quantidade):
        super().__init__(nome, cod, categoria, preco_unitario, estoque)
        self.quantidade= int(quantidade)

    @property
    #analisa se a quantidade indicada é maior que 0
    def quantidade(self):
        return self.__quant
    
    @quantidade.setter
    def quantidade(self, quant_positiva):
        if quant_positiva > 0:
            self.__quant = quant_positiva
        else:
            print("A quantidade não pode zero ou negativa. ")

    def calcular_subtotal(self):
        return self.__quant * self.preco
    
    def __str__(self):
        #apresenta as informações do item no carrinho no formato string
        subtotal = self.calcular_subtotal()
        return f"{self.nome} \nQuantidade: {self.quantidade} \nPreco Unitário: {self.preco:.2f} \nValor total: {subtotal:.2f} R$"
   

#adiciona mais itens, remove e altera quantidades
class Carrinho():
    def __init__(self):
         self.itens = []

    def __len__(self):
        return len(self.itens)
    
    def __add__(self, novo_item):
        if isinstance(novo_item, ItemCarrinho):
            self.itens.append(novo_item)
            return self
        else:
            print("Apenas itens do carrinho podem ser adicionados")
        
    def adicionar(self):
        pass
    def remover(self):
        pass

    def alterar_quant(self):
        pass

    def fechar_pedido(self):
        pass