from datetime import date
class Relatorio():
    '''A classe Relatorio é responsável por gerar os relatórios de faturamento por periodo, ranking dos produtos mais vendidos
    quantidade de vendas por Estado, categoria e status de pedidos'''
    def __init__(self, vendas, pagamentos):
        self.data_relatorio = date.today()
        self.vendas = vendas
        self.pagamentos = pagamentos
        
    def faturamento_periodo(self):
        #exibir o valor arrecadado em pedidos por periodo
        pass
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
        pass

