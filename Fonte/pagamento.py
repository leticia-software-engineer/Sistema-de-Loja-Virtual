'''A classe pagamento registra as informações do pagamento como a forma do pagamente e o seu status e valida após ser confirmado.'''
from datetime import datetime
class Pagamento():

    def __init__(self, forma_pagamento, data, status = False):
        
        data_formatada = datetime.strftime("%d/%m/%Y")

        self.forma_pagamento = str(forma_pagamento)
        self.data = data_formatada
        self.status = status
        
    def validar(self):
        #quando o status mudar para pago, a data deve ser registrada automaticamente e a forma de pagamento
        #if self.status == True:
            #self.data = 
        pass
    def registrar(self):
        pass