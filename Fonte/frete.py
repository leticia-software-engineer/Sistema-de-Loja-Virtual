'''A classe Frete é responsável por calcular o prazo e o valor do frete a partir do cep informado pelo cliente.'''
import sqlite3
import json
class Frete():
    def __init__(self, cep, arquivo = "data/ceps_cotacoes_ceara.json"):
        self.cep = cep
        self.arquivo = arquivo
    def verificar_valor_frete(self):
        with open(self.arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

        for informacao in dados:
            if informacao["cep"] == self.cep:
                self.valor = informacao["cotacao"]
                self.prazo = informacao["prazo_entrega"]
                return f"Valor do frete: {self.valor}\nPrazo de entrega: {self.prazo} dias"
            
        return "Não fazemos entrega na localidade informada."
