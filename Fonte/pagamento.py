'''A classe pagamento registra as informações do pagamento como a forma do pagamente e o seu status e valida após ser confirmado.'''
from datetime import datetime
from datetime import date
class Pagamento():

    data_formatada = date.today()#datetime.strftime("%d/%m/%Y")

    def __init__(self, forma_pagamento, data_formatada, status):
        
        self.forma_pagamento = str(forma_pagamento)
        self.data = data_formatada
        self.__status = status
        

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status_valido):
        if status_valido.lower() == "pago" or status_valido.lower() == "aguardando pagamento":
            self.__status = status_valido
        else:
            print("Status do pagamento inválido")

    def registrar(self):
        pass
    def validar(self):
        while self.__status:
            if self.__status.lower() == "pago":
                self.data = date.today()
                return f"Pagamento registrado em {self.data}"
            else:
                self.data = "Aguardando pagamento"
                return self.data
        