'''A classe Cliente armazena os dados dos clientes, tais como: nome, cpf, endereço.  Realiza operações de CRUD e faz a validação das informações do cliente.
 '''
import re
import json
class Cliente():
    def __init__(self, nome, email, cpf, rua, cep):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.rua = str(rua)
        self.cep = str(cep)

    @property
    def email(self):
        return f"Endereço de Email: {self.__email}"
    @property
    def cpf(self):
        return self.__cpf
    
    @email.setter
    def email(self, email_valido):
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.fullmatch(regex, email_valido):
            self.__email = email_valido
        else:
            print("Email invalido")
        #usar biblioteca para validar email
        pass
    @cpf.setter
    def cpf(self, cpf_validacao):
        if len(cpf_validacao) == 11:
            self.__cpf = cpf_validacao
        else:
            print("O cpf deve conter 11 dígitos.")
        
    #CRUD Realiza operações de cadastro, atualização, exclusão.
    
    def cadastrar(self):
        pass
    def ler(self):
        return "Nome: ", self.nome, "Email: ", self.email, "Cep: ", self.cep
        
    def atualizar(self):
        pass
    def deletar(self):
        
        pass
    def __str__(self):
        return f"Nome {self.nome}\nRua {self.__rua}"
        
c = Cliente("Letícia", "eule@gmail.com", "12354454515", "x", '0000')
c.cpf = "12345678910"
c.email = "eeeeee@gmail.com"
print(c.cpf)