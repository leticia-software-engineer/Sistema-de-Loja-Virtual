import re
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
    #getters
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
    @property
    def cep(self):
        return self._cep
    
    #setters
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
            raise ValueError("CPF deve conter 11 dígitos")
        
    @rua.setter
    def rua(self, rua_valida):
        if len(rua_valida) > 0 :
            self.__rua = rua_valida
        else:
            print("O nome da rua não foi informado")

    @cep.setter
    def cep(self, cep_valido):
        if len(cep_valido) == 8:
            self._cep = cep_valido
        else:
            print("O cep deve conter 8 dígitos.")
    
    def __str__(self):
        #método especial para conversão em string
        return f"Nome {self.nome_cliente}\nRua {self.__rua}"
        
#CRUD do cliente

    def cadastrar(self):
            #Conectando com o banco
            conexao = sqlite3.connect("loja virtual.db")
            cursor = conexao.cursor()

            #comando sql para procurar se já existe cadastro com o cpf informado
            sql_ler = """SELECT nome, email, rua, cep FROM cliente WHERE CPF = ?"""
            cursor.execute(sql_ler, (self.__cpf,))
            cpf_já_cadastrado = cursor.fetchone()
    
            #comando para inserir os dados no banco
            sql_inserir = """INSERT INTO cliente (nome, email, cpf, rua, cep)
            VALUES (?, ?, ?, ?, ?) """
            #dados a serem inseridos
            dados_cliente = (self.__nome, self.__email, self.__cpf, self.__rua, self.cep)
            
            if cpf_já_cadastrado:
                #se forem encontrados dados com o cpf informado
                conexao.close()
                return "Cliente já cadastrado."
            else:
                #se não forem encontrados dados com o cpf, inserir as informaçoes instanciadas
                cursor.execute(sql_inserir, dados_cliente)
                conexao.commit()
                conexao.close()
                #exibir que a operação foi bem sucedida
                return f"Cliente {self.__nome} cadastrado com sucesso. "

    def ler(self):
        
        #conecta com o banco
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()
        #buscar as informacoes da instancia no banco
        sql_ler = """SELECT nome, email, rua, cep FROM cliente WHERE CPF = ? """

        cursor.execute(sql_ler, (self.__cpf,))
        res = cursor.fetchone()
        if res:
            #se a informacao for encontrada, exibe elas
            conexao.close()
            return res
        else:
            #se não encontradas, exibe mensagem
            conexao.close()
            return "Cliente não encontrado. "

    def atualizar(self):
        
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #atualiza os dados do banco para os da instancia, menos o cpf
        sql_editar = """UPDATE cliente SET nome = ?, email = ?, rua = ?, cep = ? WHERE cpf = ?"""
        dados_cliente = (self.__nome, self.__email, self.__rua, self.cep, self.__cpf)
        cursor.execute(sql_editar, dados_cliente)
        conexao.commit()

        if cursor.rowcount > 0:
            #se alguma alteração foi feita a atualização teve sucesso
            conexao.close()
            return f"Dados do cliente {self.__nome} alterados com sucesso. "
        else:
            #se nenhuma alteração foi feita o cliente não foi encontrado
            return f"Cliente não encontrado."
        
    def deletar(self):
        
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #excluir dados do cliente com o cpf informado
        sql_deletar = """DELETE FROM cliente WHERE cpf = ?"""
        cursor.execute(sql_deletar, (self.__cpf,))
        conexao.commit()

        if cursor.rowcount > 0:
            #se informacoes foram alteradas no banco, exibe mensagem de sucesso.
            conexao.close()
            return f"Conta do cliente {self.__nome} excluída com sucesso"
        else:
            #se não foi excluída, é porque não foi encontrada
            return "Conta não encontrada."

