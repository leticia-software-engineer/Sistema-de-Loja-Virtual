import sqlite3
class Carrinho():
    '''
    A classe Carrinho é responsável por salvar os produtos escolhidos com a quantidade também escolhida pelo cliente onde serão acessados no
    momento da venda. A partir dessa classe é possível ter um controle da quantidade de itens que o cliente pretende comprar e reunir diversos produtos
    na mesma compra. Além disso, com a classe Carrinho é possível remover itens do carrinho ou alterar a quantidade sempre que um produto que já esteja no carrinho for
    novamente adicionado.
    '''

    def adicionar_carrinho(self,id_para_carrinho, codigo_produto, quantidade, com_frete):
        "Esse metódo é responsável por pegar produtos cadastrados e adicioná-los ao carrinho conforme escolha do cliente"
        self.cod = codigo_produto
        self.quantidade = quantidade
        self.frete = com_frete
        self.id_carrinho = id_para_carrinho

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
                        adicionar_no_carrinho = """INSERT INTO carrinho(cod_carrinho, nome, cod, preco, quantidade, frete) VALUES(?, ?, ?, ?, ?, ?)"""
                        dados = (self.id_carrinho, nome_produto, self.cod, preco_produto, self.quantidade, self.frete)

                        cursor.execute(adicionar_no_carrinho, dados)
                        conexao.commit()
                        conexao.close
                        return f"Produto adicionado ao carrinho."
                
                    else:
                        #se a quantidade escolhida não estiver disponível no estoque
                        return "Estoque insuficiente."
                else:
                    #se o produto já estiver no carrinho, adiciona na quantidade
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
            #se o código do produto não for informado
            return "O código do produto não foi informado."
    
    def visualizar_carrinho(self):
        #exibe a lista com os itens que estão dentro do carrinho

        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()
        #busca os itens que estão no carrinho
        visualizar = """SELECT cod_carrinho, nome, cod, preco, quantidade FROM carrinho"""
        cursor.execute(visualizar)
        itens = cursor.fetchall()
        conexao.close()

        if not itens:
            #se não forem encontrados itens
            return "Carrinho está vazio."
        else:
            #se encontrados, mostrar
            return itens
        
    def excluir_item_carrinho(self, cod):
        self.cod = cod
        #a pessoa poderá selecionar o codigo do produto que deseja remover do carrinho.
        if self.cod:
            #se o codigo que a pessoa escolheu representar um carrinho
            conexao = sqlite3.connect("loja virtual.db")
            cursor = conexao.cursor()

            #buscar as informaçoes com o codigo no carrinho
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
            #se o codigo não foi informado pelo usuário
            return "É necessário informar o código para fazer a exclusão."
        
    def __len__(self):
        #verificar quantos produtos tem em carrinhos registrados
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()
        sql_contar = "SELECT COUNT(cod) FROM carrinho"
        cursor.execute(sql_contar)
        count = cursor.fetchone()[0]
        conexao.close()
        return count
    
c = Carrinho()
print(c.adicionar_carrinho(1, 1, 2, "sim"))
print(c.adicionar_carrinho(1, 2, 1, "sim"))

print(c.visualizar_carrinho())