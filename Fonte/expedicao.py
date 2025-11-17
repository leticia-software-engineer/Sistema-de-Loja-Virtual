'''A classe expedição é responsável por armazenar as informações da entrega do produto após ele ser faturado. Essa classe vai gerar um identificador
para a entrega e marcar como entregue quando o cliente receber, e o entregador informar.'''
class Expedicao():
    def __init__(self, entrega, cod_entrega):
        self.entrega = entrega
        self.cod_entrega = cod_entrega
        pass
    def gerar_cod(self):
        pass
    def marcar_entregre(self):
        pass