'''A classe CupomDesconto armazena as informações de cupons que os clientes podem possuir dentro do sistema e aplica esse cupom quando o cliente opta
por essa aplicação em algum produto válido.'''
from datetime import date
from produto import Produto

class CupomDesconto():
    def __init__(self, cod_cupom, valor, validade):
        self.cod_cupom = cod_cupom
        self.valor = valor
        self.validade = validade

    @property
    def cod_cupom(self):
        return self.__cod_cupom
    
    @property
    def valor(self):
        return self.__valor
    
    @property
    def validade(self):
        return self.__validade
    
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
    
    @validade.setter
    def validade(self, validade_cupom):
        hoje = date.today()
        data_formatada = hoje.strftime("%d/%m/%Y")
        if validade_cupom >= data_formatada:
            self.__validade = validade_cupom
        else:
            print("Cupom vencido desde: ")
    
    def aplicar_desconto(self):
        pass

c = CupomDesconto("123456", 12, "12/10/2025", "x")
c.validade = "12/10/2025"
print(c.validade)