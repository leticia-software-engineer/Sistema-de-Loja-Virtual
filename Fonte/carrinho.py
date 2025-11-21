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
    def quantidade(self):
        return f"Quantidade no carrinho {self.__quant}"
    
    @quantidade.setter
    def quantidade(self, quant_positiva):
        if quant_positiva > 0:
            self.__quant = quant_positiva
        else:
            print("O preço não pode ser zero ou negativo. ")

    def calcular_subtotal(self):
        self.subtotal = (self.__quant * self.preco)
        return f"Total: {self.subtotal}"
    
    def __str__(self):
        subtotal = self.calcular_subtotal()
        return f"{self.nome} \nQuantidade: {self.quantidade} \nPreco Unitário: {self.preco} \nValor total: {subtotal} R$"
   
p = ItemCarrinho("abacaxi", 1111111111111, "fruta", 6, 10, 12)
p.quantidade = 12
print(p.quantidade)
print(p.calcular_subtotal())

class Carrinho(ItemCarrinho):
    
    def adicionar(self):
        pass
    def remover(self):
        pass

    def alterar_quant(self):
        pass

    def fechar_pedido(self):
        pass