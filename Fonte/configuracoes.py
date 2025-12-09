import json
import pandas

class Configuracoes():
    '''A classe Configuracoes é responsável por apresentar ao usuário opções úteis, tais como: a tabela com os prazos de envio conforme o cep, o ranking
de produtos na plataforma, o prazo de validade dos cupons, limite de parcelas e a apresentação da política de cancelamento.'''

    def __init__(self):
        pass
    def tabela_frete(self, arquivo = "data/ceps_cotacoes_ceara.json"):
        self.arquivo = arquivo
        #exibir tabela com cep e valor do frete bem como o prazo em dias para a entrega do produto
        with open(self.arquivo, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
            
            tabela = pandas.DataFrame(dados)
            return tabela

    def politica_de_cancelamento(self):
        #exibe a politica de cancelamento do sistema, explicando as regras de cancelamento de um pedido
        return "Um pedido feito na plataforma só pode ser cancelado antes do seu status ser de Enviado, sendo um prazo de até 24 horas para solicitar o cancelamento."
    def orientacoes_da_aplicacao(self):
        return "Olá! Seja bem-vindo à plataforma de vendas digital AbraCaxi, para utilizar a nossa aplicação é simples. Inicialmente você poderá visualizar os produtos que possa ter interesse, depois disso é possível adicioná-los ao carrinho mencionando os dados desse produto. Logo após, para concluir a compra, em pedido deve-se informar os dados do carrinho e fechá-lo, depois disso é só confirmar o pagamento informando o número do pedido, o tipo de pagamento, o valor e o seu status. Caso seu pedido seja de um produto físico, é possível acompanhar o status dele pela expedição utilizando o código da entrega. Caso tenha alguma dúvida na utilização da plataforma, entre em contato com nosso suporte. Contato: devv.leticia@gmail.com"
    
