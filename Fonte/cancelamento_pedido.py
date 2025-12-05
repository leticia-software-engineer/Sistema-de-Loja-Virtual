import sqlite3
from pedido import Pedido
from datetime import datetime

class CancelarPedido(Pedido):
    '''A classe CancelarPedido herda as informações da classe Pedido e é responsável por realizar o cancelamento de pedidos que ainda não foram enviados
    No caso de produtos que já foram pagos ela estorna o pagamento e o estoque, quando o pagamento ainda não foi feito ela estorna apenas o estoque
    e se o pedido já foi enviado, entregue ou cancelado ela não realiza a operação de cancelamento.'''

    def __init__(self, confirmar, confirme_cpf, confirma_cep, id_do_carrinho, num_pedido):
        super().__init__(confirmar, confirme_cpf, confirma_cep, id_do_carrinho)
        #inicializa as variáveis definindo o status como Cancelado
        self.num_pedido = num_pedido 
        self.status = "Cancelado"         

    def cancelar(self): 
        
        #faz a conexão com o banco de dados para buscar informações do pedido escolhido para cancelar
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_conferir_pedido = """SELECT produtos, status, total, data FROM pedido WHERE num_pedido = ?"""
        cursor.execute(sql_conferir_pedido, (self.num_pedido,))
        resultado = cursor.fetchone()

        if not resultado:
            #se as informacoes do pedido não forem localizadas
            conexao.close()
            return "Pedido não encontrado."
            
        
        else:
            #quando as informações são localizadas 
            #atribui uma variavel para cada indice da busca encontrado
            produtos_formatado, status_atual, valor_total, data_formatada = resultado

            if status_atual == "pago" or status_atual == "pago parcialmente":
                #estornar estoque
                conexao = sqlite3.connect("loja virtual.db")
                cursor = conexao.cursor()
                
                #tirar os dados de produto da tupla e converter para inteiro para realizar os calculos
                partes = produtos_formatado.split('; ')
                
                for parte in partes:
                    if parte.strip(): 
                        try:
                            cod_str, quantidade_str = parte.split(' (')
                            cod = int(cod_str)
                            quantidade = int(quantidade_str.strip(')'))

                            #adicionar a quantidade no estoque do produto com o codigo informado
                            sql_estornar_estoque = """ UPDATE produto SET estoque = estoque + ? WHERE cod = ? """
                            cursor.execute(sql_estornar_estoque, (quantidade, cod))
                        except ValueError:
                            pass
                #devolve o valor pago para o cliente subtraindo do pedido, o total pago volta a ser 0
                sql_estornar_pagamento = """ UPDATE pagamento SET valor_pago = 0 WHERE num_pedido = ?"""
                cursor.execute(sql_estornar_pagamento, (self.num_pedido,))

                #o status do pedido é modificado para Cancelado
                sql_alterar_status_pedido = """UPDATE pedido SET status = ? WHERE num_pedido = ?"""
                cursor.execute(sql_alterar_status_pedido, (self.status, self.num_pedido))
                
                #as informações são registradas no banco
                conexao.commit()
                conexao.close()
                return "Pedido cancelado."


            elif status_atual == "Aguardando pagamento":
                #estornar apenas estoque
                conexao = sqlite3.connect("loja virtual.db")
                cursor = conexao.cursor()
                
                partes = produtos_formatado.split('; ')
                
                for parte in partes:
                    if parte.strip(): 
                        try:
                            cod_str, quantidade_str = parte.split(' (')
                            cod = int(cod_str)
                            quantidade = int(quantidade_str.strip(')'))

                            sql_estornar_estoque = """ UPDATE produto SET estoque = estoque + ? WHERE cod = ? """
                            cursor.execute(sql_estornar_estoque, (quantidade, cod))
                        except ValueError:
                            pass
                conexao.commit()
                conexao.close()
            else:
                return f"Não é possível cancelar esse pedido."


p = CancelarPedido("sim", "11012667324", "63260000", 1, 1 )
print(p.cancelar())
