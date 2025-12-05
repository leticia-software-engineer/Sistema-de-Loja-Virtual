import uuid
from datetime import datetime, date, timedelta
import sqlite3
import json
class Expedicao():
    '''A classe expedição é responsável por armazenar as informações da entrega do produto após ele ser faturado. Essa classe vai gerar um identificador
para a entrega e marcar como entregue quando o cliente receber, e o entregador informar.'''
    def __init__(self, cod_rastreio):
        self.entrega = cod_rastreio
    
    def marcar_envio(self):

        #pegar a data do pagamento e o cod da entrega e verificar a quantidade de dias para retornar a data de entrega
        #após 24 horas do pagamento colocar o status do pedido como enviado
        #se o pedido foi feito no dia anterior alterar status para enviado
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #ver se o pedido já foi pago ou pago parcialmente
        sql_ver_pedido = """SELECT status, data FROM pedido WHERE cod_entrega = ?"""
        cursor.execute(sql_ver_pedido, (self.entrega,))
        dados = cursor.fetchone()

        status, data = dados
        data_pedido = datetime.fromisoformat(data)
        data_atual = datetime.now()

        if dados:
            if status == "pago" or status == "pago parcialmente" and data_atual - data_pedido == 1:
                status = "Enviado"

                atualizar_status = "UPDATE pedido SET status = ? WHERE cod_rastreio = ?"
                dados = (status, self.entrega)
                cursor.execute(atualizar_status, dados)
                if cursor.rowcount != 0:
                    return "Produto enviado."
                else:
                    return "Erro ao atualizar o banco de dados"
            else:
                return "Esse pedido ainda não foi enviado. Verifique nossa politica de envio."
        else:
            return "Código de rastreio não encontrado"

        
    def marcar_entregre(self):

        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #após o prazo de entrega mudar o status para entregue
        sql_ver_pedido = """SELECT status, data, confirme_cep FROM pedido WHERE cod_entrega = ?"""
        cursor.execute(sql_ver_pedido, (self.entrega,))
        dados = cursor.fetchone()

        status, data, confirme_cep = dados
        data_envio = datetime.fromisoformat(data)
        data_atual = datetime.now()
        cep_em_str = confirme_cep

        if dados:
            if status == "Enviado":
                if cep_em_str:
                    with open("data/ceps_cotacoes_ceara.json", "r", encoding="utf-8") as arquivo:
                        carregar = json.load(arquivo)
                        for item in carregar:
                            if item["cep"] == confirme_cep:
                                entrega = item["prazo_entrega"]
                                if entrega:
                                    data_entrega = data_envio + timedelta(days = entrega)
                                    if date.today() == data_entrega:
                                        atualizar_status = "UPDATE pedido SET status = ? WHERE cod_rastreio = ?"
                                        status = "Entregue"
                                        dados = (status, self.entrega)
                                        cursor.execute(atualizar_status, dados)
                                        if cursor.rowcount != 0:
                                            return "Produto enviado."
                                        else:
                                            return "Erro ao atualizar o banco de dados"
                                    else:
                                        return "O produto ainda não foi entregue"
                                else:
                                    return "Prazo de entrega não encontrado"
                            else:
                                return  "Erro ao buscar cep"
                else:
                    return "CEP não encontrado"
            else:
                return "Produto ainda não foi enviado"
        else:
            return "Dados do pedido não foram encontrados"

        
        #o prazo de entrega é dado pelo cep no arquivo json
        #a data da entrega deve ser extamente a quantidade de dias estimado depois do pedido enviado

    
