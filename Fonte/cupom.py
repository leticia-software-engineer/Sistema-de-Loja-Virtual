from datetime import date
from produto import Produto

'''Classe opcional, ainda decidindo se irei usar'''

class CupomDesconto():
    '''A classe CupomDesconto armazena as informações de cupons que os clientes podem possuir dentro do sistema e aplica esse cupom quando o cliente opta
por essa aplicação em algum produto válido.'''
    def __init__(self, cod_cupom, valor, percentual):
        self.cod_cupom = cod_cupom
        self.valor = valor
        self.percentual = percentual

    @property
    def cod_cupom(self):
        return self.__cod_cupom
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def percentual(self):
        return self.__percentual
    
    @cod_cupom.setter
    def cod_cupom(self, valida_cupom):
        if len(valida_cupom) >= 6:
            self.__cod_cupom = valida_cupom
        else:
            print("O código do cumpom deve conter pelo menos 6 dígitos. ")

    @valor.setter
    def valor(self, valida_valor):
        if valida_valor > 0:
            self.__valor = valida_valor
        else:
            print("O valor do desconto deve ser maior que 0.")
    
    @percentual.setter
    def percentual(self, percentual_cupom):
        if percentual_cupom > 0 and percentual_cupom < 100:
            self.__percentual = percentual_cupom
        else:
            print("Cupom inválido")
    