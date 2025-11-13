'''A classe Vendedor armazena os dados dos Vendedores, tais como: nome, email, cnpj e loja. 
Realiza operações de cadastro, atualização, exclusão e
também valida os dados de email e cnpj.'''
class Vendedor():
    def __init__(self, nome, email, cnpj, loja):
        self.nome = nome
        self.email = email
        self.cnpj = cnpj
        self.loja = loja
        
    #CRUD
    def cadastrar(self):
        pass
    def ler(self):
        pass
    def atualizar(self):
        pass
    def deletar(self):
        pass

    #Validação de dados
    def valida_email(self):
        pass
    def valida_cnpj(self):
        pass
    