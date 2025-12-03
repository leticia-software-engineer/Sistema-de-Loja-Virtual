import sqlite3
import json
from datetime import date
import bar_chart_race as brc
from datetime import datetime
from collections import defaultdict
class Relatorio():
    '''A classe Relatorio é responsável por gerar os relatórios de faturamento por periodo, ranking dos produtos mais vendidos
    quantidade de vendas por Estado, categoria e status de pedidos'''
    def __init__(self):
        self.data_relatorio = date.today()
        
    def faturamento_periodo(self):
        
        #conexao com banco 
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()
        sql_visualizar_pagamentos = """SELECT valor_pago, data_pagamento FROM pagamento"""
        cursor.execute(sql_visualizar_pagamentos)
        pagamentos = cursor.fetchall()
        conexao.close()

        #conferindo pagamentos
        if not pagamentos: 
            return {}
        else:
            faturamento_por_mes = defaultdict(float)
            faturamento_por_dia = defaultdict(float)
            for valor_pago, data_pagamento_formatada in pagamentos:
            
                try:
                    data = datetime.strptime(data_pagamento_formatada, '%Y-%m-%d').date()
                except ValueError:
                    continue 
                
                valor = float(valor_pago)
                mes = data.strftime('%Y-%m') 
                dia = data.strftime('%Y-%m-%d')
                faturamento_por_mes[mes] += valor
                faturamento_por_dia[dia] += valor
        
        relatorio_data = {
            "data_geracao": date.today().strftime('%Y-%m-%d'),
            "faturamento_mensal": dict(faturamento_por_mes),
            "faturamento_diario": dict(faturamento_por_dia)
        }
            
        
        json_string = json.dumps(relatorio_data, indent=4) 
        nome_arquivo = "relatorio_faturamento.json"
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(json_string)
        return f"Relatório de faturamento gerado com sucesso no arquivo: {nome_arquivo}"
        

    def ranking(self):
        #mostrar produtos mais vendidos
        pass
    def vendas_por_estado(self):
        #mostrar quantidade de vendas feitas para cada estado
        pass
    def vendas_por_categoria(self):
        #mostrar a quantidade de vendas feitas em cada categoria de produto
        pass
    def pedidos_status(self):
        #mostrar o status dos pedidos - pago, aguardando pagamento.
        #quantidade de pedidos com status pago e aguardando pagamento
        pass

r = Relatorio()
print(r.faturamento_periodo())