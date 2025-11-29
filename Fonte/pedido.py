import uuid
import sqlite3
from datetime import datetime
from pagamento import Pagamento
from carrinho import Carrinho
from frete import Frete
from cupom import CupomDesconto
from expedicao import Expedicao

class Pedido():
    '''A classe Pedido armazena todos os dados da compra e a partir das informações gera um cupom da venda, além disso ela é responsável por permitir 
o cancelamento de um pedido seguindo as políticas de cancelamento informadas nas configurações.'''

    def __init__(self, carrinho: Carrinho, pagamento: Pagamento, frete: Frete, expedicao: Expedicao, cupom = None):
        self.carrinho = carrinho
        self.pagamento = pagamento
        self.frete = frete
        self.expedicao = expedicao
        self.cupom = cupom
        self.cod_pedido = str(uuid.uuid4())
        self.data_pedido = datetime.now()
        self.status = "Aguardando Pagamento"
        
    def calcular_subtotal_com_frete(self):
        pass
    def fechar_pedido(self):
        #pegar os itens do carrinho e fechar o pedido
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        sql_conferir_carrinho = """SELECT * FROM carrinho WHERE COD = ?"""
        pass
    def faturar(self):
        #salvar as informacoes do pagamento
        pass
    def informacoes_da_entrega(self):
        #exibir prazo esperado para a entrega 
        pass
    def __str__(self):
        return f"Pedido: {self.cod_pedido} | Cliente: {self.nome} | Total: R${self.calcular_total():.2f} | Status: {self.status}"
        

       