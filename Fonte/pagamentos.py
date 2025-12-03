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

        sql_conferir_pagamentos= """SELECT valor_pago FROM pagamento WHERE id_pedido= ?"""
        cursor.execute(sql_conferir_pagamentos, (self.num_do_pedido,))
        encontrado = cursor.fetchone()
        sql_conferir_pedido = """SELECT total, status FROM pedido WHERE num_pedido= ?"""
        cursor.execute(sql_conferir_pedido, (self.num_do_pedido,))
        total = cursor.fetchone()
        if total:
            #verificar se o status já está como pago
            status = total[1]
            if status == "pago":
                return "Esse pedido já foi pago."
            elif status == "pago parcialmente":
                
                valor_pago = encontrado[0]
                valor_a_pagar = total[0] - valor_pago
                if self.valor_pago <= valor_a_pagar:
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
                        "Falha ao registrar pagamento."
                else:
                    return "O valor digitado é maior que o valor devido. "
            else:
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
                    "Falha ao registrar pagamento."
        else: 
            return "Pedido não encontrado"

    def alterar_status_pedido(self):
        if self.status.lower() == "pago":
            self.data_pagamento = date.today()

            conexao = sqlite3.connect("loja virtual.db")
            cursor = conexao.cursor()

            sql_alterar_status_pedido = """UPDATE pedido SET status = ? WHERE num_pedido = ?"""
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
            

p = Pagamento(1, "pix", 245, "pago")
print(p.registrar_pagamento())
