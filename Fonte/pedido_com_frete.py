import sqlite3
from pedido import Pedido

class PedidoComFrete(Pedido):
    def __init__(self, confirmar, confirme_cpf):
        super().__init__(confirmar, confirme_cpf)
        self.confirme_cep = confirme_cpf
    
    def mostrar_cotacao(self):
        pass
    def conferir_frete(self):
        conexao = sqlite3.connect()
        cursor = conexao.cursor()
        sql_confere_se_frete = """SELECT frete FROM carrinho WHERE frete = ?"""
        cursor.execute(sql_confere_se_frete, ("sim",))
        result = cursor.fetchall()
        if not result:
            conexao.close()
            Pedido.calcular_subtotal
        else:
            subtotal = subtotal + self.frete
            return subtotal
