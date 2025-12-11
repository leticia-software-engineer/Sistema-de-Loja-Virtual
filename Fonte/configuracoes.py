import json
import pandas

class Configuracoes():
    '''A classe Configuracoes é responsável por apresentar ao usuário opções úteis, tais como: a tabela com os prazos de envio conforme o cep, o ranking
de produtos na plataforma, o prazo de validade dos cupons, limite de parcelas e a apresentação da política de cancelamento.'''

    def tabela_frete(self, arquivo = "data/ceps_cotacoes_ceara.json"):
        self.arquivo = arquivo
        #exibir tabela com cep e valor do frete bem como o prazo em dias para a entrega do produto
        with open(self.arquivo, "r", encoding="utf-8") as arq:
            dados = json.load(arq)
            
            tabela = pandas.DataFrame(dados)
            return tabela

    def politica_de_cancelamento(self, arquivo = "settings.json"):
        #exibe a politica de cancelamento do sistema, explicando as regras de cancelamento de um pedido
        self.arquivo = arquivo
        with open(self.arquivo, "r", encoding="utf-8") as config:
            dados = json.load(config)

            configuracoes = dados.get("CONFIGURACOES", {})
            
            politica = configuracoes.get("POLITICA_CANCELAMENTO", "Política de cancelamento não configurada.")

            return politica

    def orientacoes_da_aplicacao(self, arquivo = "settings.json"):
        self.arquivo = arquivo
        with open(self.arquivo, "r", encoding="utf-8") as config:
            dados = json.load(config)

            configuracoes = dados.get("CONFIGURACOES", {})

            orientacoes = configuracoes.get("ORIENTACOES_APLICACAO")
            return orientacoes
    

