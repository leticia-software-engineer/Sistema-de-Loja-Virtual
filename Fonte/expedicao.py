'''A classe expedição é responsável por armazenar as informações da entrega do produto após ele ser faturado. Essa classe vai gerar um identificador
para a entrega e marcar como entregue quando o cliente receber, e o entregador informar.'''
import uuid
from datetime import date

# resolver geração de codigo

class Expedicao():
    def __init__(self, entrega = date):
        self.entrega = entrega
        #self.__cod_entrega = cod_entrega
        pass
    def gerar_cod(self):
        self.cod_entrega = uuid.uuid4()
        return self.cod_entrega
    def marcar_entregre(self):
        pass
    
