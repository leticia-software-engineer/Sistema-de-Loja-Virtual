'''Deve registrar e realizar operações com os produtos, tais como:
    cadastro, leitura, atualização e exclusão,
bem como deverá fazer ajustes em caso de movimentação do estoque.'''
    
class Produto():
    
    def __init__(self, nome, cod, categoria, preco_unitario, estoque):
        self.nome = nome
        self.cod = cod
        self.categoria = categoria
        self.preco_unitario = preco_unitario
        self.estoque = estoque
    
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
        