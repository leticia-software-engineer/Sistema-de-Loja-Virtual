'''Deve registrar e realizar operações com os produtos, tais como:
    cadastro, leitura, atualização e exclusão,
bem como deverá fazer ajustes em caso de movimentação do estoque.'''
import json
    
class Produto():
    
    def __init__(self, nome, cod, categoria, preco_unitario, estoque, arquivo = "data/produtos.json"):
        self.nome = nome
        self.cod = cod
        self.categoria = categoria
        self.preco = preco_unitario
        self.estoque_valido = estoque
        self.arquivo = arquivo

    @property
    def preco(self):
        return f"{self.preco_unitario} R$"
    @property
    def estoque_valido(self):
        return f"{self.estoque} unidades "
    
    @preco.setter
    def preco(self, preco_positivo):
        if preco_positivo > 0:
            self.preco_unitario = preco_positivo
        else:
            raise ValueError("O preço não pode ser zero ou negativo. ")

    @estoque_valido.setter
    def estoque_valido(self, estoque_v):
        if estoque_v >= 0:
            self.estoque = estoque_v
        else:
            raise ValueError("O valor do estoque não pode ser negativo. ")

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
    def __str__(self):
        return f"Produto {self.nome}\nCódigo {self.cod}\nCategoria {self.categoria}\nEstoque {self.estoque}\nPreço {self.preco_unitario}"
    

c = Produto("abacaxi", 1, "fruta", 6, 23)
print(c)

