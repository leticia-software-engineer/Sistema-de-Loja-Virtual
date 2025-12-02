import re
import requests
import sqlite3
class Cliente():
    '''A classe Cliente armazena os dados dos clientes, tais como: nome, cpf, endereço.  Realiza operações de CRUD e faz a validação das informações do cliente.
 '''
    def __init__(self, nome_cliente, email, cpf, rua, cep):
        self.nome_cliente = nome_cliente
        self.email = email
        self.cpf = cpf
        self.rua = str(rua)
        self.cep = str(cep)

    '''decoradores property com funçoes getters e setters para validar as informações de nome_cliente, email, cpf e rua além de adicionar encapsulamento a esses atributos'''
    @property
    def nome_cliente(self):
        return self.__nome
    @property
    def email(self):
        return self.__email
    @property
    def cpf(self):
        return self.__cpf
    @property
    def rua(self):
        return self.__rua
    
    @nome_cliente.setter
    def nome_cliente(self, nome_valido):
        if len(nome_valido) > 2:
            self.__nome = nome_valido
        else: 
            print("Comprimento de nome_cliente inválido")
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
    @rua.setter
    def rua(self, rua_valida):
        if len(rua_valida) > 0 :
            self.__rua = rua_valida
        else:
            print("O nome da rua não foi informado")
    
    #CRUD Realiza operações de cadastro, atualização, exclusão.
    
    def cadastrar(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()
        sql_ler = """SELECT nome, email, rua, cep FROM cliente WHERE CPF = ?"""

        sql_inserir = """INSERT INTO cliente (nome, email, cpf, rua, cep)
         VALUES (?, ?, ?, ?, ?) """
        dados_cliente = (self.__nome, self.__email, self.__cpf, self.__rua, self.cep)

        cursor.execute(sql_ler, (self.__cpf,))
        res = cursor.fetchone()
   
        if res:
            return "Cliente já cadastrado."
        else:
            cursor.execute(sql_inserir, dados_cliente)
            conexao.commit()
            conexao.close()
            return f"Cliente {self.__nome} cadastrado com sucesso. "

    def ler(self):
        
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_ler = """SELECT nome, email, rua, cep FROM cliente WHERE CPF = ? """

        cursor.execute(sql_ler, (self.__cpf,))
        res = cursor.fetchone()
        if res:
            conexao.close()
            return res
        else:
            conexao.close()
            return "Cliente não encontrado. "

    def atualizar(self):
        
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_editar = """UPDATE cliente SET nome = ?, email = ?, rua = ?, cep = ? WHERE cpf = ?"""
        dados_cliente = (self.__nome, self.__email, self.__rua, self.cep, self.__cpf)

        cursor.execute(sql_editar, dados_cliente)
        conexao.commit()

        if cursor.rowcount > 0:
            conexao.close()
            return f"Dados do cliente {self.__nome} alterados com sucesso. "
        else:
            return f"Cliente não encontrado."
        
    def deletar(self):
        
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_deletar = """DELETE FROM cliente WHERE cpf = ?"""

        cursor.execute(sql_deletar, self.__cpf)
        conexao.commit()

        if cursor.rowcount > 0:
            conexao.close()
            return f"Conta do cliente {self.__nome} excluída com sucesso"
        else:
            return "Conta não encontrada."
    def __str__(self):
        return f"Nome {self.nome_cliente}\nRua {self.__rua}"
        

c = Cliente("Joao", "joao@gmail.com", "12345678910", "São José", "63210000")
c2 = Cliente("Jose", "jose@gmail.com", "12345678911", "São José", "63210000")
print(c.cadastrar())
print(c2.cadastrar())

print(c.ler())
print(c2.ler())
