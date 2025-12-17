import sqlite3
from Fonte.produto import Produto

class ProdutoFisico(Produto):

    '''A classe ProdutoFisico herda de produto todos os seus atributos e métodos e possui metodos e atributos adicionais que são
    o CRUD, que adiciona, lê, atualiza e deleta informacoes desses produtos do banco de dados e possui o atributo frete como obrigatório'''
   
    def __init__(self, nome, codigo, categoria, preco_unitario, estoque, frete = "sim"):
        super().__init__(nome, codigo, categoria, preco_unitario, estoque)
        self.nome = nome
        self.__cod = str(codigo)
        self.categoria = categoria
        self.__preco = float(preco_unitario)
        self.__estoque = estoque
        self.frete = frete

#CRUD
    def cadastrar(self):
        
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #Confere se já existe algum produto com o codigo escolhido pelo usuario cadastrado para algum outro produto
        sql_checar = "SELECT cod FROM produto WHERE cod = ?"
        cursor.execute(sql_checar, (self.__cod,))
        pesq = cursor.fetchone()

        #se não encontra adiciona no banco
        if pesq == None:
            sql_inserir = """
            INSERT INTO produto(nome, cod, categoria, preco, estoque, frete)
            VALUES(? ,? ,? ,? ,?, ? )
            """
            dados_produto = (self.nome, self.__cod, self.categoria, self.__preco, self.__estoque, self.frete)

            cursor.execute(sql_inserir, dados_produto)
            conexao.commit()
            conexao.close()
            return f"Produto {self.nome} cadastrado com sucesso."
           
        else: 
            #se encontra não adiciona
            conexao.close()
            return "Já existe um produto cadastrado com esse codigo"


    @classmethod
    def listar(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_buscar = """SELECT nome, cod, categoria, preco, estoque FROM produto"""
        cursor.execute(sql_buscar)
        resultado = cursor.fetchall() 
        
        if resultado: 
            conexao.close()
            return resultado
        else:
            conexao.close()
            return "Produtos não encontrados"

    def ler(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_buscar = """SELECT nome, cod, categoria, preco, estoque, frete FROM produto WHERE COD = ? and NOME = ?"""

        cursor.execute(sql_buscar, (self.cod, self.nome))
        resultado = cursor.fetchone() 
        
        if resultado: 
            conexao.close()
            return resultado
        else:
            conexao.close
            return "Produto não encontrado"
    
    def atualizar(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_editar = """UPDATE produto SET nome = ? , categoria = ?, preco = ?, estoque = ? WHERE cod = ?"""

        dados_produto = (self.nome, self.categoria, self.__preco, self.__estoque, self.__cod)
        cursor.execute(sql_editar, dados_produto)
        conexao.commit()
        
        if cursor.rowcount > 0:
            conexao.close()
            return f"Produto {self.nome} atualizado com sucesso."
        else:
            return "Produto não encontrado"
        
    
    def deletar(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_deletar = """DELETE FROM produto WHERE cod = ?"""
        cursor.execute(sql_deletar, (self.__cod,))
        
        conexao.commit()
        if cursor.rowcount:
            conexao.close()
            return f"Produto {self.nome} excluido com sucesso."
        else:
            conexao.close()
            return f"Produto não encontrado para excluir."

    def __repr__(self):
        return f"Produto(nome='{self.nome}', cod='{self.__cod}', preco={self.__preco}, estoque={self.__estoque})"
    
    def __eq__(self, outro):
        if not isinstance(outro, ProdutoFisico):
            return NotImplemented
        return self.__cod == outro.__cod
    
class LerProdutos():

    def __init__(self, cod):
        self.cod = cod
    def ler(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_buscar = """SELECT nome, cod, categoria, preco FROM produto WHERE COD = ?"""

        cursor.execute(sql_buscar, (self.cod,))
        resultado = cursor.fetchone() 
        
        if resultado: 
            conexao.close()
            return resultado
        else:
            conexao.close()
            return "Produto não encontrado"