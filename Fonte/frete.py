'''A classe Frete é responsável por calcular o prazo e o valor do frete a partir do cep informado pelo cliente.'''
import requests
from cliente import Cliente
class Frete(Cliente):
    def __init__(self, nome, email, cpf, rua, cep):
        super().__init__(nome, email, cpf, rua, cep)

    def valida_cep(self):
    
        if len(self.cep) != 8:
            print("Cep inválido")
            exit()
        
        requisicao = requests.get(f'https://viacep.com.br/ws/{self.cep}/json/')
        if "erro" in requisicao.json():
            return "Cep inválido"
        else:    
            req = requisicao.json()
            self.cep = f"Cep: {req['cep']}\nCidade: {req['localidade']}\nUF: {req['uf']}"
            return self.cep
           
    def calcular_por_cep(self):
        pass

f = Frete("Letícia", "eule@gmail.com", "12345678910", "maria x", '63260000')
print(f.valida_cep())