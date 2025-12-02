import sqlite3
import json
from datetime import date, datetime
from collections import defaultdict


class Relatorio():

    def arrecadacao_mensal(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_visualizar_pagamentos = """
        SELECT valor_pago, data_pagamento FROM pagamento
        """
        cursor.execute(sql_visualizar_pagamentos)
        pagamentos = cursor.fetchall()
        conexao.close()

        if not pagamentos:
            # Retorna um dicionário vazio para indicar que não há dados
            return {} 
        
        faturamento_por_mes = defaultdict(float)
        faturamento_por_dia = defaultdict(float)
        
        for valor_pago, data_pagamento_str in pagamentos:
            
            try:
                data_obj = datetime.strptime(data_pagamento_str, '%Y-%m-%d').date()
            except ValueError:
                continue 

            chave_mes = data_obj.strftime('%Y-%m') 
            chave_dia = data_obj.strftime('%Y-%m-%d')
            
            #try:
            valor = float(valor_pago)
            #except ValueError:
            #    continue 

            faturamento_por_mes[chave_mes] += valor
            faturamento_por_dia[chave_dia] += valor
        
        # Converte os defaultdicts para dicts normais e os acumula no resultado final
        relatorio_data = {
            "data_geracao": date.today().strftime('%Y-%m-%d'),
            "faturamento_mensal": dict(faturamento_por_mes),
            "faturamento_diario": dict(faturamento_por_dia)
        }
            
        return relatorio_data # Retorna a estrutura de dados Python (dict)

    def faturamento_periodo(self):
        # 1. Obter a estrutura de dados (dicionário)
        relatorio_data = self.arrecadacao_mensal()
        
        # 2. Verificar se há dados
        if not relatorio_data:
            return "Nenhum pagamento encontrado para gerar o relatório JSON."
            
        # 3. Serializar o dicionário para uma string JSON formatada
        try:
            # O indent=4 serve para formatar o JSON de forma legível
            json_string = json.dumps(relatorio_data, indent=4) 
        except Exception as e:
             return f"Erro ao serializar para JSON: {e}"

        # 4. Salvar a string JSON em um arquivo
        nome_arquivo = "relatorio_faturamento.json"
        
        try:
            # Abre o arquivo para escrita ('w')
            with open(nome_arquivo, 'w', encoding='utf-8') as f:
                f.write(json_string)
                
            return f"Relatório de faturamento gerado com sucesso no arquivo: **{nome_arquivo}**"
        
        except Exception as e:
            return f"Erro ao escrever o arquivo JSON: {e}"

    # ... (código para as outras funções)

r = Relatorio()
print(r.faturamento_periodo())