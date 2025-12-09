import sqlite3
from datetime import date
class Pagamento():
    '''A classe pagamento registra as informações do pagamento como a forma do pagamente e o seu status e valida após ser confirmado.'''

    def __init__(self, num_pedido, forma_pagamento, valor_pago, status):
        
        self.forma_pagamento = str(forma_pagamento)
        self.status = status
        self.valor_pago = valor_pago
        self.data_pagamento = date.today()
        self.num_do_pedido = num_pedido

    def registrar_pagamento(self):
        
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_conferir_pagamentos= """SELECT SUM(valor_pago) FROM pagamento WHERE num_pedido= ?"""
        cursor.execute(sql_conferir_pagamentos, (self.num_do_pedido,))
        encontrado = cursor.fetchone()
        

        sql_conferir_pedido = """SELECT total, status FROM pedido WHERE num_pedido= ?"""
        cursor.execute(sql_conferir_pedido, (self.num_do_pedido,))
        total = cursor.fetchone()
        
        self.valor_a_pagar = total[0] - self.valor_pago

        if total:
            #verificar se o status já está como pago
            status = total[1]
            if status == "pago":
                return "Esse pedido já foi pago."
            elif status == "pago parcialmente":
                
                self.valor_pago = encontrado[0]
                self.valor_a_pagar = total[0] - self.valor_pago
                if self.valor_pago <= self.valor_a_pagar:
                    sql_salvar_pagamento = """INSERT INTO pagamento (id_pedido, forma_pagamento, valor_pago, data_pagamento)
                    VALUES (?, ?, ?, ?)"""
                    dados_pagamento = (self.num_do_pedido, self.forma_pagamento, self.valor_pago, self.data_pagamento)

                    cursor.execute(sql_salvar_pagamento, dados_pagamento)
                    conexao.commit()

                    sql_alterar_status_pedido = """UPDATE pedido SET status = ? WHERE num_pedido = ?"""
                    status_mudar = (self.status, self.num_do_pedido)
                    cursor.execute(sql_alterar_status_pedido, status_mudar)
                    conexao.commit()
                    if cursor.rowcount > 0:
                        conexao.close()
                        return "Pagamento registrado"
                    else:
                        conexao.close()
                        "Falha ao registrar pagamento."
                else:
                    return "O valor digitado é maior que o valor devido. "
            else:
                sql_salvar_pagamento = """INSERT INTO pagamento (num_pedido, forma_pagamento, valor_pago, data_pagamento)
                VALUES (?, ?, ?, ?)"""
                dados_pagamento = (self.num_do_pedido, self.forma_pagamento, self.valor_pago, self.data_pagamento)

                cursor.execute(sql_salvar_pagamento, dados_pagamento)
                conexao.commit()

                if cursor.rowcount != 0:
                    sql_alterar_status_pedido = """UPDATE pedido SET status = ? WHERE num_pedido = ?"""
                    status_mudar = (self.status, self.num_do_pedido)
                    cursor.execute(sql_alterar_status_pedido, status_mudar)
                    conexao.commit()
                    conexao.close()
                    return "Pagamento registrado"
                else:
                    "Falha ao registrar pagamento."
            
        else: 
            return "Pedido não encontrado"

    def alterar_status_pedido(self):
        if self.status.lower() == "pago":
            self.data_pagamento = date.today()

            conexao = sqlite3.connect("loja virtual.db")
            cursor = conexao.cursor()

            sql_alterar_status_pedido = """UPDATE pedido SET status = ? WHERE cod_carrinho = ?"""
            status_mudar = (self.status, self.num_do_pedido)
            cursor.execute(sql_alterar_status_pedido, status_mudar)
            conexao.commit()
        
            if cursor.rowcount > 0:
                conexao.close()
                return "Status do pagamento registrado com sucesso!"
            else:
                conexao.close()
                return "Pagamento não registrado."
        else:
            return "O pagamento só é registrado após sua confirmação."
        
    def atualizar_estoque(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_consultar_pedido = """SELECT produtos FROM pedido WHERE num_pedido = ?"""
        cursor.execute(sql_consultar_pedido, (self.num_do_pedido,))
        resultado = cursor.fetchone()

        if resultado == None:
            conexao.close()
            return "Pedido não encontrado."

        produtos = resultado[0]  # primeira coluna do SELECT

        if produtos.strip() == "":
            conexao.close()
            return "Pedido não possui produtos."

        produtos_lista = [p.strip() for p in produtos.split(';') if p.strip()]

        for item in produtos_lista:
           
            cod, quantidade_str = item.split(' (')
            cod = cod.strip()
            quantidade = int(quantidade_str.replace(')', '').strip())
           

            sqlconsultarproduto = """SELECT estoque FROM produto WHERE cod = ?"""
            cursor.execute(sqlconsultarproduto, (cod,))
            produtoencontado = cursor.fetchone()

            estoque_atual = produtoencontado[0]
            novo_estoque = estoque_atual - quantidade

            # atualizar estoque
            sql_alterar_estoqueproduto = """UPDATE produto SET estoque = ? WHERE cod = ?"""
            cursor.execute(sql_alterar_estoqueproduto, (novo_estoque, cod))

        conexao.commit()
        conexao.close()
        return "Estoque atualizado com sucesso."
