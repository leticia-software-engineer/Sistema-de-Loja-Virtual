import sqlite3
from pagamento import Pagamento
from datetime import date

class PagarParcelado(Pagamento):
    #Classe filha de Pagamento para pagamento ser realizado em parcelas
    def __init__(self, forma_pagamento, status, num_parcelas):
        super().__init__(forma_pagamento, status)
        self.num_parcelas = num_parcelas
        self.valor_parcelas = None


    @property 
    def num_parcelas(self):
        return self.__parcelas
    @num_parcelas.setter
    def num_parcelas(self, parcela_valida):
        if parcela_valida > 1:
            self.__parcelas = parcela_valida
        else:
            print("Para pagamento parcelado o número de parcelas deve ser maior que 1. ")

    def calcular_valor_parcelas(self):
        self.valor_parcelas = self.subtotal_pedido/ self.num_parcelas
        #cada parcela deve ser paga 30 dias depois da anterior até a ultima parcela ser paga
        pass

    def pagamento_parcelas(self):
        #datas e valores a serem pagos
        self.data_parcelas = None
        self.valor_parcelas = None

    def confirmacao_pagamento(self):
        #confirma o recebimento da parcela.
        pass

   