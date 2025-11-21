'''Deve registrar e realizar operações com os produtos, tais como:
    cadastro, leitura, atualização e exclusão,
bem como deverá fazer ajustes em caso de movimentação do estoque.'''
import json
    
class Produto():
    
    def __init__(self, nome, codigo, categoria, preco_unitario, estoque, arquivo = "data/produtos.json"):
        self.nome = nome
        self.cod = str(codigo)
        self.categoria = categoria
        self.preco = float(preco_unitario)
        self.estoque_valido = estoque
        self.arquivo = arquivo

    @property
    def cod(self):
        return f"Código GTIN: {self.__cod}"
    @property
    def preco(self):
        return self.__preco
    @property
    def estoque_valido(self):
        return f"{self.__estoque} unidades no estoque"
    
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

    @estoque_valido.setter
    def estoque_valido(self, estoque_v):
        if estoque_v >= 0:
            self.__estoque = estoque_v
        else:
            print("O valor do estoque não pode ser negativo. ")

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
        pass
    '''def __str__(self):
        return f"Produto {self.nome}\nCódigo {self.cod}\nCategoria {self.categoria}\nEstoque {self.estoque}\nPreço {self.preco_unitario}"
   ''' 

c = Produto("abacaxi", 1, "fruta", 6, 1)
c.preco = 6
c.estoque_valido = 100
c.cod = "1234567891012"
print(c.preco)
print(c.estoque_valido)
print(c.cod)

