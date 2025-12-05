import sqlite3
import json
from datetime import date
import bar_chart_race as brc
from datetime import datetime
from collections import defaultdict
from collections import Counter

class Relatorio():
    '''A classe Relatorio é responsável por gerar os relatórios de faturamento por periodo, ranking dos produtos mais vendidos
    quantidade de vendas por Estado, categoria e status de pedidos'''
    def __init__(self):
        self.data_relatorio = date.today()
        
    def faturamento_periodo(self):
        
        #conexao com banco 
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #procurar as informacoes de valores e datas dos pagamentos feitos
        sql_visualizar_pagamentos = """SELECT valor_pago, data_pagamento FROM pagamento"""
        cursor.execute(sql_visualizar_pagamentos)
        pagamentos = cursor.fetchall()
        conexao.close()

        #conferindo pagamentos
        if not pagamentos: 
            return "Nenhum pagamento encontrado"
        else:
            #se pagamentos forem encontrados seram gerados dois dicionarios, faturamento por mes e por dia
            faturamento_por_mes = defaultdict(float)
            faturamento_por_dia = defaultdict(float)
            for valor_pago, data_pagamento_formatada in pagamentos:
            #para cada pagamento encontrado converter as datas que estiverem no formato de string para o formato date
                try:
                    data = datetime.strptime(data_pagamento_formatada, '%Y-%m-%d').date()
                except ValueError:
                    continue 
                
                #atribuindo valor as variaveis
                valor = float(valor_pago)
                mes = data.strftime('%Y-%m') 
                dia = data.strftime('%Y-%m-%d')
                #incrementando os valores nos dicionarios
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
        #conexao com banco 
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #procurar as informacoes de valores e datas dos pagamentos feitos
        sql_visualizar_pedidos = """SELECT produtos FROM pedido"""
        cursor.execute(sql_visualizar_pedidos)
        produtos_codigo_quantidade = cursor.fetchall()
        conexao.close()

        #se forem encontrados produtos vendidos
        if produtos_codigo_quantidade:
            codigos = [item[0] for item in produtos_codigo_quantidade]
            contar_codigos = Counter(codigos)

            ranking = contar_codigos.most_common()

            for codigo, quantidade in ranking:

                sql_visualizar_produtos = """SELECT nome FROM produto WHERE cod = ?"""
                cursor.execute(sql_visualizar_produtos, codigo)
                nome_do_produto = cursor.fetchone()
                print(f"Produto Código: {nome_do_produto} - Vendido: {quantidade} vezes")

                #guardar no json
                json_string = json.dumps(ranking, indent=4) 
                nome_arquivo = "ranking.json"
                with open(nome_arquivo, 'w', encoding='utf-8') as f:
                    f.write(json_string)
                return f"Ranking de produtos vendidos salvo em: {nome_arquivo}"
                

        else:
            return "Nenhum pedido encontrado."

    def vendas_por_cep(self):
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