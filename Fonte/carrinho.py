'''
A classe ItemCarrinho é responsável por salvar os produtos escolhidos pelo cliente em uma parte específica da memória onde serão acessados no
momento da venda a partir dessa classe é possível ter um controle da quantidade de itens que o cliente pretende comprar e reunir diversos produtos
na mesma compra. Além disso, com a classe Carrinho é possível remover do carrinho ou alterar a quantidade daqueles produtos que o cliente desejar.
'''
from produto import Produto

class ItemCarrinho(Produto):
    def __init__(self, nome, cod, categoria, preco_unitario, estoque, quantidade):
        super().__init__(nome, cod, categoria, preco_unitario, estoque)
        self.quant= quantidade

    @property
    def quantidade(self):
        return self.quant
    
    @quantidade.setter
    def quantidade(self, quant_positiva):
        if quant_positiva > 0:
            self.quant = quant_positiva
        else:
            raise ValueError("O preço não pode ser zero ou negativo. ")
    def calcular_subtotal(self):
        subtotal = self.preco_unitario * self.quantidade
        return subtotal
    
    def __str__(self):
        subtotal = self.calcular_subtotal()
        return f"{self.nome} \nQuantidade: {self.quant} \nPreco Unitário: {self.preco_unitario} \nValor total: {subtotal} R$"
   
p = ItemCarrinho("abacaxi", 1, "fruta", 6, 10, 12)
p2 = ItemCarrinho("uva", 2, "fruta", 2, 20, 10)
print(p)
print(p2)

class Carrinho(ItemCarrinho):
    
    def adicionar(self):
        pass
    def remover(self):
        pass

    def alterar_quant(self):
        pass

    pass