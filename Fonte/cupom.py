'''A classe CupomDesconto armazena as informações de cupons que os clientes podem possuir dentro do sistema e aplica esse cupom quando o cliente opta
por essa aplicação em algum produto válido.'''
class CupomDesconto():
    def __init__(self, cod_cupom, valor, validade, caso_uso):
        self.cod_cupom = cod_cupom
        self.valor = valor
        self.validade = validade
        self.caso_uso = caso_uso

    def aplicar_desconto(self):
        pass