'''A classe Relatorio é responsável por gerar os relatórios de faturamento por periodo, ranking dos produtos mais vendidos
quantidade de vendas por Estado, categoria e status de pedidos'''
from datetime import date
class Relatorio():
    def __init__(self, vendas, pagamentos):
        self.data_relatorio = date.today()
        self.vendas = vendas
        self.pagamentos = pagamentos
        
    def faturamento_periodo(self):
        pass
    def ranking(self):
        pass
    def vendas_por_estado(self):
        pass
    def vendas_por_categoria(self):
        pass
    def pedidos_status(self):
        pass

