import uuid
import sqlite3
from datetime import datetime
#from carrinho import Carrinho as car

class Pedido():
    '''A classe Pedido armazena todos os dados da compra e a partir das informações gera um cupom da venda, além disso ela é responsável por permitir 
o cancelamento de um pedido seguindo as políticas de cancelamento informadas nas configurações.'''

    def __init__(self, confirmar, confirme_cpf, id_do_carrinho):
        
        self.cod_pedido = str(uuid.uuid4())
        self.data_pedido = datetime.now()
        self.confirmar = str(confirmar)
        self.confirme_cpf = confirme_cpf
        self.total = 0
        self.cod_carrinho_pedido = id_do_carrinho

    def calcular_subtotal(self):
        #calcula primeiro o subtotal dos produtos que estão no carrinho
        conec = sqlite3.connect("loja virtual.db")
        cursor = conec.cursor()
        sql_ver_precos = """SELECT nome, preco, quantidade FROM carrinho"""
        cursor.execute(sql_ver_precos)
        resultado = cursor.fetchall()
        self.total = 0
        for produto in resultado:
                
            preco = produto[1]
            quantidade = produto[2]
            subtotal = preco * quantidade 
            self.total = subtotal + self.total
            
        return self.total
            
    def fechar_pedido(self):
        if self.confirmar.lower() != "sim":
            return "Pedido não confirmado foi cancelado."
        else:
            #pegar os itens do carrinho e fechar o pedido
            conexao = sqlite3.connect("loja virtual.db")
            cursor = conexao.cursor()
            sql_ver_cliente = """SELECT nome FROM cliente WHERE cpf = ?"""
            cursor.execute(sql_ver_cliente, (self.confirme_cpf,))
            cliente_encontrado = cursor.fetchall()

            if cliente_encontrado:
                sql_conferir_carrinho = """SELECT nome, preco, quantidade FROM carrinho"""
                cursor.execute(sql_conferir_carrinho)
                carrinho = cursor.fetchall()
                
                if carrinho:
                    self.data = datetime.now()
                    status = "Aguardando pagamento"
                    produtos_str = []
                    for produto in carrinho:
                        nome, preco, quantidade = produto
                        produtos_str.append(f"{nome} ({quantidade}) - R${preco:.2f}")

                    produtos_para_db = "; ".join(produtos_str)
                                        
                    #fechar o pedido  
                    sql_insert_pedido = """
                    INSERT INTO pedido (data, cliente_cpf, total, status, cod_carrinho, produtos)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """
                    data_formatada = self.data.isoformat()
                    valores = (data_formatada, self.confirme_cpf, Pedido.calcular_subtotal(self), status, self.cod_carrinho_pedido, produtos_para_db)
                    
                    cursor.execute(sql_insert_pedido, valores)
                    conexao.commit()
                    sql_esvaziar_carrinho = """DELETE FROM carrinho WHERE cod_carrinho = ?"""
                    cursor.execute(sql_esvaziar_carrinho, (self.cod_carrinho_pedido,))
                    conexao.commit()
                    conexao.close()
                    return "Pedido salvo, aguardando pagamento."
                else:
                    conexao.close()
                    return "Não foram encontradas informações no carrinho"
    def visualizar_pedidos(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        visualizar = """SELECT * from pedido where cliente_cpf = ?"""
        cursor.execute(visualizar, (self.confirme_cpf,))
        r_busca = cursor.fetchall()
        if r_busca:
            self.cod_carrinho_pedido = r_busca[0][0]
            conexao.close()
            
            return r_busca
        else:
            return "Não foram encontrados pedidos desse cliente."
            
    def informacoes_da_entrega(self):
        #exibir prazo esperado para a entrega 
        pass
    def __str__(self):
        return f"Pedido: {self.cod_pedido} | Cliente: {self.nome} | Total: R${self.calcular_total():.2f} | Status: {self.status}"
    
p = Pedido("sim", "12345678910", 1)
print(p.visualizar_pedidos())