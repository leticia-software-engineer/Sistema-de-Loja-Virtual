'''A classe Cliente armazena os dados dos clientes, tais como: nome, cpf, endereço. Realiza operações de cadastro, atualização, exclusão e
também valida os dados de email, cpf e cep.'''
class Cliente():
    def __init__(self, nome, email, cpf, cidade, cep, uf):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.cidade = cidade
        self.cep = cep
        self.uf = uf
        
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
    def valida_cep(self):
        pass

