#para gerar a nota é só digitar o numero do pedido
import sqlite3

class NotaFiscal():
    #apenas exibe as informacoes do pedido que o usuario desejar ver
    def __init__(self, num_pedido: int):
        self.num_pedido = num_pedido

    def vernota(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        selecionandopedido = """SELECT * FROM pedido WHERE num_pedido = ? """
        cursor.execute(selecionandopedido, (self.num_pedido,))

        nota = cursor.fetchall()

        if nota != None:
            return nota
        
        else:
            return "Pedido não encontrado" 