'''A classe Frete é responsável por calcular o prazo e o valor do frete a partir do cep informado pelo cliente.'''
import sqlite3
import json
class Frete():
    def __init__(self, cep: str, arquivo = "data/ceps_cotacoes_ceara.json"):
        self.cep = cep
        self.arquivo = arquivo
    def verificar_valor_frete(self):
        #abre o arquivo json
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        #busca o cep que o usuario digitou ao iterar sobre cada valor de cep nos dicionarios bem como seu valor e prazo de entrega
        for informacao in dados:
            if informacao["cep"] == self.cep:
                self.valor = informacao["cotacao"]
                self.prazo = informacao["prazo_entrega"]
                #retorna o resultado da busca
                
                return f"Valor do frete: {self.valor} Prazo de entrega: {self.prazo} dias"
            
        return "Não fazemos entrega na localidade informada."
