'''A classe Relatorio é responsável por gerar os relatórios de faturamento por periodo, ranking dos produtos mais vendidos
quantidade de vendas por Estado, categoria e status de pedidos'''
import json
class Relatorio():
    def __init__(self, dia, mes, ano, vendas, pagamentos):
        self.dia = dia
        self.__mes = mes
        self.__ano = ano
        self.vendas = vendas
        self.__pagamentos = pagamentos
        
        @property
        def dia(self):
            return self.__dia
        @dia.setter
        def dia(self, dia_valido):
            if len(dia_valido) == 2:
                dia_valido = self.__dia
            else:
                print("O dia deve coonter apenas dois dígitos")

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