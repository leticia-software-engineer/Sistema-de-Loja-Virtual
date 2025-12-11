import sqlite3
class Produto():
    '''Deve servir como molde de produto trazendo propriedades com getters e setters e dados de inicialização 
    comuns a qualquer produto, bem como métodos especiais'''    

    def __init__(self, nome: str, codigo: int, categoria: str, preco_unitario: float, estoque: int):
        #variáveis comuns em qualquer produto
        self.nome = nome
        self.cod = str(codigo)
        self.categoria = categoria
        self.preco = float(preco_unitario)
        self.estoque = estoque

    #getters para codigo, preco e estoque com encapsulamento
    @property
    def cod(self):
        return self.__cod
    @property
    def preco(self):
        return self.__preco
    @property
    def estoque(self):
        return self.__estoque
    
    #setters para codigo, preco e estoque com encapsulamento 
    @cod.setter
    def cod(self, codigo_valido):
        #define que o codigo do produto não pode ser 0 ou negativo
        if len(codigo_valido) > 0:
            self.__cod = codigo_valido 
        else:
            raise ValueError("Codigo do produto não pode ser vazio")

    @preco.setter
    def preco(self, preco_positivo):
        #informa que preco de produto nao pode 0 ou negativo
        if preco_positivo > 0:
            self.__preco = preco_positivo
        else:
            raise ValueError("O preço não pode ser zero ou negativo. ")

    @estoque.setter
    def estoque(self, estoque_v):
        if estoque_v >= 0:
            #define que do estoque no momento da sua inserção não pode ser 0 ou negativo
            self.__estoque = estoque_v
        else:
            raise ValueError("O valor do estoque não pode ser negativo. ")

    