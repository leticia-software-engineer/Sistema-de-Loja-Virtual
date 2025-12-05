import uuid
import json
import sqlite3
from datetime import datetime
#from carrinho import Carrinho as car

class Pedido():
    '''A classe Pedido armazena todos os dados da compra e a partir das informações gera um cupom da venda, além disso ela é responsável por permitir 
o cancelamento de um pedido seguindo as políticas de cancelamento informadas nas configurações.'''

    def __init__(self, confirmar, confirme_cpf, confirma_cep, id_do_carrinho):
        
        self.data_pedido = datetime.now()
        self.confirmar = str(confirmar)
        self.confirme_cpf = confirme_cpf
        self.total = 0
        self.num_pedido = id_do_carrinho
        self.confirmar_cep = confirma_cep
        self.cod_entrega = None
        self.total_pedido = 0

        
        #iniciando as variáveis
        self.total = 0
        self.arquivo = None
        self.frete = 0

    def calcular_subtotal(self, arquivo = "data/ceps_cotacoes_ceara.json"):
        #calcula primeiro o subtotal dos produtos que estão no carrinho
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        #verifica os valores dos produtos no carrinho
        sql_ver_precos = """SELECT nome, preco, quantidade FROM carrinho"""
        cursor.execute(sql_ver_precos)
        resultado = cursor.fetchall()

        #verifica se é um pedido com frete incluso
        sql_confere_se_frete = """SELECT frete FROM carrinho WHERE frete = ?"""
        cursor.execute(sql_confere_se_frete, ("sim",))
        result = cursor.fetchall()

        #iniciando as variáveis
        self.total = 0
        self.arquivo = arquivo
        self.frete = 0

        if not result:
            for produto in resultado:
                    
                preco = produto[1]
                quantidade = produto[2]
                subtotal = preco * quantidade 
                self.total += subtotal
                
            return self.total
        else:

            #verifica o cep do cliente 
            procurar_cep_do_cliente =  """SELECT cep FROM cliente WHERE cpf = ?"""
            cursor.execute(procurar_cep_do_cliente, (self.confirme_cpf,))
            cep_do_cliente = cursor.fetchone()
            for produto in resultado:
                    
                preco = produto[1]
                quantidade = produto[2]
                subtotal = preco * quantidade 
                self.total += subtotal
                

            if cep_do_cliente:
                
                cep_do_cliente = str(cep_do_cliente[0]) 
            else:
                conexao.close()
                return "Não foi possível encontrar o CEP do cliente." 
        
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                frete_encontrado = False

                for informacao in dados:
                    cep_cadastrado_json = informacao["cep"]
                    if cep_cadastrado_json == cep_do_cliente:
                        self.frete = informacao["cotacao"]
                        self.total += self.frete
                        frete_encontrado = True
                        break
                if frete_encontrado == True:
                    return self.total
           
            
    def fechar_pedido(self):
        if self.confirmar.lower() != "sim":
            return "Pedido não confirmado foi cancelado."
        elif self.total == 0:
            return "Subtotal não calculado."
        else:
            #pegar os itens do carrinho e fechar o pedido
            conexao = sqlite3.connect("loja virtual.db")
            cursor = conexao.cursor()
            sql_ver_cliente = """SELECT nome FROM cliente WHERE cpf = ?"""
            cursor.execute(sql_ver_cliente, (self.confirme_cpf,))
            cliente_encontrado = cursor.fetchall()

            if cliente_encontrado:
                sql_conferir_carrinho = """SELECT cod, quantidade FROM carrinho WHERE cod_carrinho= ?"""
                cursor.execute(sql_conferir_carrinho, (self.num_pedido,))
                carrinho = cursor.fetchall()
                
                if carrinho:
                    self.data = datetime.now()
                    status = "Aguardando pagamento"
                    produtos_str = []
                    for produto in carrinho:
                        cod, quantidade = produto
                        produtos_str.append(f"{cod} ({quantidade})")

                    produtos_para_db = "; ".join(produtos_str)
                                        
                    #fechar o pedido  
                    sql_insert_pedido = """
                    INSERT INTO pedido (data, cliente_cpf, total, status, cod_carrinho, produtos, frete, cod_entrega, confirme_cep)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """
                    data_formatada = self.data.isoformat()
                    valores = (data_formatada, self.confirme_cpf, self.total, status, self.num_pedido, produtos_para_db, self.frete, self.cod_entrega, self.confirmar_cep)
                    
                    cursor.execute(sql_insert_pedido, valores)
                    conexao.commit()
                    sql_esvaziar_carrinho = """DELETE FROM carrinho WHERE cod_carrinho = ?"""
                    cursor.execute(sql_esvaziar_carrinho, (self.num_pedido,))
                    conexao.commit()
                    conexao.close()
                    
                    return "Pedido salvo, aguardando pagamento."
                else:
                    conexao.close()
                    return "Não foram encontradas informações no carrinho"
            else:
                return "Cliente não encontrado."
    def visualizar_meus_pedidos(self):
        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        visualizar = """SELECT * from pedido where cliente_cpf = ?"""
        cursor.execute(visualizar, (self.confirme_cpf,))
        r_busca = cursor.fetchall()
        if r_busca:
            self.num_pedido = r_busca[0][0]
            conexao.close()
            
            return r_busca
        else:
            conexao.close()
            return "Não foram encontrados pedidos desse cliente."
            
    def informacoes_da_entrega(self, id_pedido):

        conexao = sqlite3.connect("loja virtual.db")
        cursor = conexao.cursor()

        visualizar = """SELECT num_pedido, frete, cod_entrega from pedido where num_pedido = ?"""
        cursor.execute(visualizar, (id_pedido,))
        pedido = cursor.fetchone()

        if pedido:
            idpedido, frete, cod_entrega = pedido
            frete_formatado = float(frete)
            if id_pedido == idpedido and frete_formatado > 0 and cod_entrega == None:
                self.cod_entrega = str(uuid.uuid1())
                atualizar = """UPDATE pedido SET cod_entrega = ? WHERE num_pedido = ?"""

                cursor.execute(atualizar, (self.cod_entrega, id_pedido))
                conexao.commit()

                if cursor.rowcount > 0:
                    return f"Pedido habilitado para frete. Código de rasteamento {self.cod_entrega}"

            else:
                return "Pedido não habilitado para frete."
        else:
            return "Pedido não encontrado."
        

p = Pedido("sim", "11012667324", 63260000, 4)

print(p.visualizar_meus_pedidos())
                
        
        
    