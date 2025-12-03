import uuid
from datetime import date

class Expedicao():
    '''A classe expedição é responsável por armazenar as informações da entrega do produto após ele ser faturado. Essa classe vai gerar um identificador
para a entrega e marcar como entregue quando o cliente receber, e o entregador informar.'''
    def __init__(self, cod_rastreio):
        self.entrega = cod_rastreio
    
    def rastrear_entrega(self):

        #pegar a data do pagamento e o cod da entrega e verificar a quantidade de dias para retornar a data de entrega
        #após 24 horas do pagamento colocar o status do pedido como enviado
        pass
    def marcar_entregre(self):
        #após o prazo de entrega mudar o status para entregur
        pass
    
