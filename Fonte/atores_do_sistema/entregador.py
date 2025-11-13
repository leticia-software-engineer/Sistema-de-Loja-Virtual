'''A classe Entregador armazena os dados dos entregadores, tais como: nome, email, cpf, distribuidora, cnh. 
Realiza operações de cadastro, atualização, exclusão e
também valida os dados de email e cpf.'''
class Entregador():
    def __init__(self, nome, email, cpf, distribuidora, cnh):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.distribuidora = distribuidora
        self.cnh = cnh
        
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
    def valida_cpf(self):
        pass
   