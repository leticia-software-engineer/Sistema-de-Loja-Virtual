import sqlite3
import json
from datetime import date
from datetime import datetime
from collections import defaultdict
from collections import Counter

class Relatorio():
    '''A classe Relatorio é responsável por gerar os relatórios de faturamento por periodo, ranking dos produtos mais vendidos
    quantidade de vendas por Estado, categoria e status de pedidos'''
    def __init__(self):
        #a data da geração do relatório é guardada na variavel self.data_relatorio
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
        
        #organizando o dicionario
        relatorio_data = {
            "data_geracao": date.today().strftime('%Y-%m-%d'),
            "faturamento_mensal": dict(faturamento_por_mes),
            "faturamento_diario": dict(faturamento_por_dia)
        }
            
        #criando o arquivo json com as informacoes
        json_string = json.dumps(relatorio_data, indent=4) 
        nome_arquivo = "relatorio_faturamento.json"
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(json_string)
        return f"Relatório de faturamento gerado com sucesso no arquivo: {nome_arquivo}"
        

    def pedidos_por_cep(self):
        #mostrar quantidade de vendas feitas para cada cep
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #procurar as informacoes de valores e datas dos pagamentos feitos
        sql_visualizar_pedidos = """SELECT confirme_cep FROM pedido"""
        cursor.execute(sql_visualizar_pedidos)
        cep_pedidos = cursor.fetchall()

        if not cep_pedidos:
            return "Não foi encontrado nenhum pedido"
        else:
            lista_de_ceps = []
            #pegar cada cep, e colocar numa lista
            for cep in cep_pedidos:
                lista_de_ceps.append(cep)

            #pegar a lista e fazer a contagem de cada item
            contar = Counter(lista_de_ceps)
            dicionario = dict(contar)
            dicionario_para_guardar = {cep_em_tupla[0]: quant for cep_em_tupla, quant in dicionario.items()}
            arquivo_relatorio_por_cep = "relatorio por cep.json"
            with open(arquivo_relatorio_por_cep, "w", encoding="utf-8") as arquivo:
                    
            #salvar no arquivo json o cep e a quantidade de vendas para ele
                json.dump(dicionario_para_guardar, arquivo, ensure_ascii=False, indent=4)
                return f"Relatorio de pedidos por cep gerado em {arquivo_relatorio_por_cep}"
                #return f"Relatório de cep gerado no arquivo {arquivo_relatorio_por_cep}"
        
    def pedidos_por_status(self):
        #mostrar quantidade de pedidos com cada status
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #procurar as informacoes de status dos pedidos feitos
        sql_visualizar_pedidos = """SELECT status FROM pedido"""
        cursor.execute(sql_visualizar_pedidos)
        status_pedidos = cursor.fetchall()

        if not status_pedidos:
            return "Não foi encontrado nenhum pedido"
        else:
            lista_status_encontrados = []
            #para cada pedido encontrado pegar o status adicionar numa lista e contar os itens da lista usando Counter
            for status in status_pedidos:
                lista_status_encontrados.append(status)
            contar = Counter(lista_status_encontrados)
            #criar dicionario com as informacoes
            dicionario = dict(contar)

            dicionario_para_guardar = {status_em_tupla[0]: quant for status_em_tupla, quant in dicionario.items()}
            quantidade_total = 0
            #criar listas para porcentagens para cada status
            porcentagens = []
            lista_status_porcentagem = []

            #Pegar os valor do dicionario para guardar e fazer a soma da quantidade total de status encontrados um por pedido
            for quantidade in dicionario_para_guardar.values():
                pedidos_por_status = quantidade
                quantidade_total += quantidade

            #Fazer o calculo da porcentagem iterando por cada status e guardar na lista de porcentagens
            for status in dicionario_para_guardar.values():
                porcentagem = (status/quantidade_total)*100
                porcentagens.append(f'{porcentagem: .2f} %')
            
        #distribuir para cada chave key do dicionario a respectiva porcentagem na lista
           
            for chave, quantidade in dicionario_para_guardar.items():
                porcentagem = (quantidade / quantidade_total) * 100
                
                # Adiciona a chave e a porcentagem correspondente
                lista_status_porcentagem.append(chave)
                lista_status_porcentagem.append(f'{porcentagem: .2f} %')

        #guardar os dados do relatório no json
        relatorio_pedidos_status = "relatorio de pedidos por status.json"                    
        with open(relatorio_pedidos_status, "w", encoding="utf-8") as arquivo:
            json.dump(dicionario_para_guardar, arquivo, ensure_ascii=False, indent=4)
        return f"Essa foi a porcentagem encontrada para cada status {lista_status_porcentagem} Para mais detalhes leia as quantidades de pedidos para cada status no arquivo {relatorio_pedidos_status}"            
