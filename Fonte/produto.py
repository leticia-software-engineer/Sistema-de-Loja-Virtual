import sqlite3
class Produto():
    '''Deve registrar e realizar operações com os produtos, tais como:
    cadastro, leitura, atualização e exclusão,
    bem como deverá fazer ajustes em caso de movimentação do estoque.'''    

    def __init__(self, nome, codigo, categoria, preco_unitario, estoque):
        self.nome = nome
        self.cod = str(codigo)
        self.categoria = categoria
        self.preco = float(preco_unitario)
        self.estoque = estoque

    @property
    def cod(self):
        return self.__cod
    @property
    def preco(self):
        return self.__preco
    @property
    def estoque(self):
        return self.__estoque
    
    @cod.setter
    def cod(self, codigo_valido):
        if len(codigo_valido) > 0:
            self.__cod = codigo_valido 
        else:
            print("Codigo do produto não pode ser vazio")

    @preco.setter
    def preco(self, preco_positivo):
        if preco_positivo > 0:
            self.__preco = preco_positivo
        else:
            print("O preço não pode ser zero ou negativo. ")

    @estoque.setter
    def estoque(self, estoque_v):
        if estoque_v >= 0:
            self.__estoque = estoque_v
        else:
            print("O valor do estoque não pode ser negativo. ")

    def __str__(self):
        return f"Produto: {self.nome} custa {self.__preco} R$"
    
    def __repr__(self):
        return f"Produto(nome='{self.nome}', cod='{self.__cod}', preco={self.__preco}, estoque={self.__estoque})"
    
    #CRUD
    def cadastrar(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_checar = "SELECT cod FROM produto WHERE cod = ?"
        cursor.execute(sql_checar, (self.__cod,))
        pesq = cursor.fetchone()

        if pesq == None:
            sql_inserir = """
            INSERT INTO produto(nome, cod, categoria, preco, estoque)
            VALUES(? ,? ,? ,? ,? )
            """
            dados_produto = (self.nome, self.__cod, self.categoria, self.__preco, self.__estoque)

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

        sql_buscar = """SELECT nome, cod, categoria, preco, estoque FROM produto WHERE COD = ?"""

        cursor.execute(sql_buscar, (self.cod,))
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
        dados_produto = (self.nome, self.categoria, self.__preco, self.__estoque, self.__cod)

        cursor.execute(sql_deletar, (self.__cod,))
        
        conexao.commit()
        if cursor.rowcount:
            conexao.close()
            return f"Produto {self.nome} excluido com sucesso."
        else:
            conexao.close()
            return f"Produto não encontrado para excluir."

    def ajustar_estoque_entrada(self):
        #controlar estoque dos produtos
        #se um produto for atualizado e for acrescentado estoque, seu estoque seve ser atualizado.
        #se uma venda for cancelada o estoque deve ser estornado
        
        pass
    def ajustar_estoque_saida(self):
        #controlar estoque dos produtos
        #após confirmação de pedido o estoque do produto deve ser subtraído
        pass

p = Produto("teste", "4", "teste", 12, 100)
p.cadastrar()