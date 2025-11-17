'''A classe Cliente armazena os dados dos clientes, tais como: nome, cpf, endereço. 
 '''

class Cliente():
    def __init__(self, nome, email, cpf, cidade, cep, uf):
        self.nome = nome
        self.__email = email
        self.__cpf = cpf
        self.__cidade = cidade
        self.__cep = cep
        self.__uf = uf

    
    #CRUD Realiza operações de cadastro, atualização, exclusão.
    
    def cadastrar(self):
        pass
    def ler(self):
        return "Nome: ", self.nome, "Email: ", self.__email, "Cep: ", self.__cep
        pass
    def atualizar(self):
        pass
    def deletar(self):
        pass

    #Validação de dados: valida os dados de email, cpf e cep.
    
    def valida_email(self):
        pass
    def valida_cpf(self):
        
        pass
        
