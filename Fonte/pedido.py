
class Pedido():
    def __init__(self, cliente, itens, frete, desconto, total, status):
        self.itens = itens
        self.total = total
        self.status = status
        pass
    def cancelar(self):
        pass
    def gerar_nota(self):
        pass