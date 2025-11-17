'''A classe Relatorio é responsável por gerar os relatórios de faturamento por periodo, ranking dos produtos mais vendidos
quantidade de vendas por Estado, categoria e status de pedidos'''
class Relatorio():
    def __init__(self, dia, mes, ano, vendas, pagamentos):
        self.dia = dia
        self.mes = mes
        self.ano = ano
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
