'''Deve registrar e realizar operações com os produtos, tais como:
    cadastro, leitura, atualização e exclusão,
bem como deverá fazer ajustes em caso de movimentação do estoque.'''
import json
    
class Produto():
    
    def __init__(self, nome, codigo, categoria, preco_unitario, estoque):
        self.nome = nome
        self.__cod = str(codigo)
        self.categoria = categoria
        self.__preco = float(preco_unitario)
        self.__estoque = estoque

    @property
    def cod(self):
        return self.__cod
    @property
    def preco(self):
        return self.__preco
    @property
    def estoque(self):
        return self.__estoque
    
    @cod.setter
    def cod(self, codigo_valido):
        if len(codigo_valido) == 13:
            self.__cod = codigo_valido 
        else:
            print("Codigo de barras deve conter 13 digitos")

    @preco.setter
    def preco(self, preco_positivo):
        if preco_positivo > 0:
            self.__preco = preco_positivo
        else:
            print("O preço não pode ser zero ou negativo. ")

    @estoque.setter
    def estoque(self, estoque_v):
        if estoque_v >= 0:
            self.__estoque = estoque_v
        else:
            print("O valor do estoque não pode ser negativo. ")

    def __str__(self):
        return f"Produto: {self.nome} custa {self.__preco} R$"
    
    def __repr__(self):
        return f"Produto(nome='{self.nome}', cod='{self.__cod}', preco={self.__preco})"
    

class GerenciarEstoque():
    #CRUD
    def cadastrar(self):
        pass

    def ler(self):
        pass
    def atualizar(self):
        pass
    def deletar(self):
        pass

    def ajustar_estoque(self):
        #controlar estoque dos produtos
        pass

    