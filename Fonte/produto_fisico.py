import sqlite3
from produto import Produto

class ProdutoFisico(Produto):
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

        sql_checar = "SELECT cod FROM produto WHERE cod = ?"
        cursor.execute(sql_checar, (self.__cod,))
        pesq = cursor.fetchone()
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
            conexao.close()
            return "Já existe um produto cadastrado com esse codigo"


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

p = ProdutoFisico("Teste", 1, "teste", 12, 10)
print(p.cadastrar())
p1 = ProdutoFisico("Sabão", 2, "limpeza", 8, 100)
print(p1.cadastrar())
a = ProdutoFisico("Abacaxi", 3, "fruta", 6, 4)
print(a.cadastrar())