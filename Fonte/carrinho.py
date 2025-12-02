import sqlite3
class Carrinho():
    '''
    A classe Carrinho é responsável por salvar os produtos escolhidos com a quantidade também escolhida pelo cliente onde serão acessados no
    momento da venda. A partir dessa classe é possível ter um controle da quantidade de itens que o cliente pretende comprar e reunir diversos produtos
    na mesma compra. Além disso, com a classe Carrinho é possível remover itens do carrinho ou alterar a quantidade sempre que um produto que já esteja no carrinho for
    novamente adicionado.
    '''
    def __init__(self, nome, codigo, quantidade, com_frete):
        self.nome = nome
        self.cod = codigo
        self.quantidade = quantidade
        self.frete = com_frete

    def __len__(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()
        sql_contar = "SELECT COUNT(cod) FROM carrinho"
        cursor.execute(sql_contar)
        count = cursor.fetchone()[0]
        conexao.close()
        return count
    
    def adicionar_carrinho(self):
        #metodo para adicionar produtos ao carrinho.
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        if self.cod:
            #verificar se o produto escolhido pelo usuario existe
            verificar_produto_existe = """SELECT nome, cod, categoria, preco, estoque FROM produto WHERE cod = ?"""
            cursor.execute(verificar_produto_existe, (self.cod,))
            resultado = cursor.fetchone() 
             
            if not resultado: 
                #se o produto não existir
                conexao.close()
                return f"Produto com codigo {self.cod} não encontrado"
            #se o produto existir
            else:
                
                #verificar se o produto já está no carrinho
                verificar_carrinho = """SELECT nome, cod, preco, quantidade FROM carrinho WHERE cod = ?"""
                cursor.execute(verificar_carrinho, (self.cod,))
                res = cursor.fetchone() 

                        
                if not res: 
                    #se o produto não estiver no carrinho ainda
                    nome_produto = resultado[0] 
                    preco_produto = resultado[3]
                    estoque = resultado[4]
                    if estoque >= self.quantidade:
                        #se a quantidade escolhida for maior que o estoque disponível para o produto, permitir adicao ao carrinho
                        adicionar_no_carrinho = """INSERT INTO carrinho(nome, cod, preco, quantidade, frete) VALUES(?, ?, ?, ?, ?)"""
                        dados = (nome_produto, self.cod, preco_produto, self.quantidade, self.frete)

                        cursor.execute(adicionar_no_carrinho, dados)
                        conexao.commit()
                        conexao.close
                        return f"Produto adicionado ao carrinho."
                
                    else:
                        return "Estoque insuficiente."
                else:
                    #se o produto já estiver no carrinho
                    quantidade_atual = res[3]
                    estoque_atual = resultado[4]
                    nova_quantidade = quantidade_atual + self.quantidade
                    if estoque_atual >= nova_quantidade:
                        #verificar se o estoque é suficiente para a adicao
                        atualizar_no_carrinho = """UPDATE carrinho SET quantidade = ? WHERE cod = ?"""
                        dados_update = (nova_quantidade, self.cod)
                        cursor.execute(atualizar_no_carrinho, dados_update)
                        conexao.commit()
                        conexao.close()
                        return "Produto adicionado ao carrinho"
                    else:
                        return "Estoque insuficiente."
        else:
            return "O código do produto não foi informado."
    
    def visualizar_carrinho(self):
        #exibe a lista com os itens que estão dentro do carrinho
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        visualizar = """SELECT cod_carrinho, nome, cod, preco, quantidade FROM carrinho"""
        cursor.execute(visualizar)
        itens = cursor.fetchall()
        conexao.close()

        if not itens:
            return "Carrinho está vazio."
        else:
            return itens
        
    def excluir_item_carrinho(self):
        #a pessoa poderá selecionar o codigo do produto que deseja remover do carrinho.
        if self.cod:
            conexao = sqlite3.connect("loja virtual.db")
            cursor = conexao.cursor()
            procurar_item_carrinho = """SELECT nome, cod, preco, quantidade FROM carrinho WHERE cod = ?"""
            cursor.execute(procurar_item_carrinho, (self.cod,))
            produto_encontrado = cursor.fetchone()

            if produto_encontrado:
            #se o codigo for encontrado a exclusão é realizada
                deletar_item_carrinho = """DELETE FROM carrinho WHERE cod = ?"""
                cursor.execute(deletar_item_carrinho, (self.cod,))
                conexao.commit()
                conexao.close()
                return "Produto removido com sucesso"
            else:
                #se o codigo não é encontrado, uma mensagem é exibida
                conexao.close()
                return "Produto não encontrado no carrinho"
        
        else:
            return "É necessário informar o código para fazer a exclusão."
        



c1 = Carrinho(
    "Ebook sei lá", "10", 3, "sim"
)
print(c1.adicionar_carrinho())

print(c1.visualizar_carrinho())



