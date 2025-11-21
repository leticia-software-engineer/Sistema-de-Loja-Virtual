'''A classe Relatorio é responsável por gerar os relatórios de faturamento por periodo, ranking dos produtos mais vendidos
quantidade de vendas por Estado, categoria e status de pedidos'''
import json
class Relatorio():
    def __init__(self, data_relatorio, vendas, pagamentos):
        self.data_relatorio = data_relatorio
        self.vendas = vendas
        self.__pagamentos = pagamentos
        
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

c = Relatorio("0", "02", "2006", "20", "100")

c.dia = "0"
print(c.dia)