'''A classe Frete é responsável por calcular o prazo e o valor do frete a partir do cep informado pelo cliente.'''

#Token do melhor envio: eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiNjE4YmUxNjRjM2VhYTk0OTM4ZTc2ZTBiZDYxYmY1ZGY0MmJmNmZhYTQ3Y2E5NmFiZmMyMWUwOTIzNGIwMGZhZDM1MGRmMGFmODgxOWRkZWEiLCJpYXQiOjE3NjQ0NjQzOTEuNTc4ODAyLCJuYmYiOjE3NjQ0NjQzOTEuNTc4ODAzLCJleHAiOjE3OTYwMDAzOTEuNTY5MTAyLCJzdWIiOiJhMDdhMWQzZi1hNDU4LTQyNjUtOTIwOC03Yzk5YTliNmFmOTEiLCJzY29wZXMiOlsib3JkZXJzLXJlYWQiLCJwdXJjaGFzZXMtcmVhZCIsInNoaXBwaW5nLWNhbGN1bGF0ZSIsInNoaXBwaW5nLWNhbmNlbCIsInNoaXBwaW5nLWdlbmVyYXRlIl19.a3cAT7n0E9UY63WKevDzgO7fPYCs8iGPV5TviOwhLrT0Od6ZUAWmH4jkjpyhTgjz5o9I-W6j4XU11WqdSq2z6UlY9eELk7s7mb0g3pvlcE3Up3HSHUdWO9r4wPvrUI6NaDJAqgWBpbSY84QiP4eVyL_090jQgucQAfD8X_K4JDjLuP8F0avKsF7IsHX9fBO-xEb-pdUKxTNdbixV1Z1SLyTNeJlWxSiu-OuU2dDns0R8TKxO6oFYm7uX2nMSzE0NRSNv2bCr5u18WM6y_QK5RUrKbAf9OZZdMgrpqRuCPxwgBK3qkGHAJ31sGOb_7hxoEkDUAdi_GWj3NYR13Qidl1_XCcBxGfumldESqcMgvvN5Es-K_lkUfrSg2ThJ8rNqeSf2Bj72tZvom-C4Z-nZCYlBYHrqFi-TcBXby0BYkdF9GdiJnQLI9Da0HDiIqc21wlaJbWxX3ORmbV3Ku-t1nYQY7wgs-UxTgf81N7tbbJq6HtpXHjc2Y6_3NNI-O-C5UO3RXnBMPxqr8GC8kdwm6mZxq4xhqM_O72EHxuIPV_LLY7VBeU_wam-i0VeaY2HUEJIu79R_KeU0KcDKpKNpaT74oOnalZ3as2qP91idJD6IRVyQmMn67nIffrm8POBNkJwi-VzAmm1FsTN7H3w_lChIAdlNBM2U2QohOlpAQSE
# request https://sandbox.melhorenvio.com.br/api/v2/me/shipment/calculate
import requests
import json
from cliente import Cliente
class Frete():
    def __init__(self, cep):
        self.cep = cep
        self.cep_formatado = None
    def validar_cep(self):
    
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
           
    def calcular_valor_frete_por_cep(self):
        #requisicao melhor envio
        url = "https://sandbox.melhorenvio.com.br/api/v2/me/shipment/calculate"
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiOTZiOWM0MjEwNjdjNGZkYjEzZmQyODA3ZDljMzE0YWI3MDVhMWI0Y2ZiYmJiMzYxY2UyN2U3OGIzMzM2NmFiMGFhOTkzODUxNTlkYWU1NjYiLCJpYXQiOjE3NjQ1MjM4NTAuODk1NzIyLCJuYmYiOjE3NjQ1MjM4NTAuODk1NzI0LCJleHAiOjE3OTYwNTk4NTAuODg0MjE1LCJzdWIiOiJhMDdhMWQzZi1hNDU4LTQyNjUtOTIwOC03Yzk5YTliNmFmOTEiLCJzY29wZXMiOlsiY2FydC1yZWFkIiwiY2FydC13cml0ZSIsImNvbXBhbmllcy1yZWFkIiwiY29tcGFuaWVzLXdyaXRlIiwiY291cG9ucy1yZWFkIiwiY291cG9ucy13cml0ZSIsIm5vdGlmaWNhdGlvbnMtcmVhZCIsIm9yZGVycy1yZWFkIiwicHJvZHVjdHMtcmVhZCIsInByb2R1Y3RzLWRlc3Ryb3kiLCJwcm9kdWN0cy13cml0ZSIsInB1cmNoYXNlcy1yZWFkIiwic2hpcHBpbmctY2FsY3VsYXRlIiwic2hpcHBpbmctY2FuY2VsIiwic2hpcHBpbmctY2hlY2tvdXQiLCJzaGlwcGluZy1jb21wYW5pZXMiLCJzaGlwcGluZy1nZW5lcmF0ZSIsInNoaXBwaW5nLXByZXZpZXciLCJzaGlwcGluZy1wcmludCIsInNoaXBwaW5nLXNoYXJlIiwic2hpcHBpbmctdHJhY2tpbmciLCJlY29tbWVyY2Utc2hpcHBpbmciLCJ0cmFuc2FjdGlvbnMtcmVhZCIsInVzZXJzLXJlYWQiLCJ1c2Vycy13cml0ZSIsIndlYmhvb2tzLXJlYWQiLCJ3ZWJob29rcy13cml0ZSIsIndlYmhvb2tzLWRlbGV0ZSIsInRkZWFsZXItd2ViaG9vayJdfQ.eAqOc8p_Z78M2Eok0KMlBbgcGwOQ3dmNrvs126h98_0u2FGLJWY_ZImZnhi_pFvuGcfHOhNdOtVpk1ckzN_dlN8QZI_c-KYf8Hy0ukIhZ5rIZ2piC583KCa2vn6kC6IFcUBsYmDy9Gs7AJ6ONvInCAa_gQX31dLqXLY12GUlxMCHWVf7RSYRUJL-kfyrVMEmezvudDKT-CVNaWkjW3iJRopA6_hjwvOTKuzPxjL2GcVC-OBsx1rsbIN3clfbrTZ_vXjqsFyYPwa6DoSy2n55Y3-7GFa6kU1kVtYXl8xYDlE4bCWal0f5er887Nik9bm3Zo_EoXN4woHR9bhprCjx5UcjDuWpBWrrDMyF-SFpOeXs2h-t2zTUyE8YZMhcjP4ERfyPu5lGRVchhLsPwmkNMI_S_1GgY6QExhwGAdHwGg2oulG411y-v-I__UjxLO0mjypoVwD0WQ2znoJHFepLQ-WX-GNknuyE85zkxu8VmQCdZb9gV15tV8sGev89EIxjU9nBqwx_36CbauAkfDvjfDECd0kLxoToInXRwdKw-EJjPrcDC1zvMWU5cMgXiYP20Xx9RGaRugiZ_BNKNrMgZJYjtO-u6wzAfPiRa4D3tHLqjkKJ0Bbm4VPngQc-cMObo6ZsJqKLiNO5Xxn9L838mTIeb1Lrda6iHh-mNy9XqzA"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": token,
            "User-Agent": "euleticiadias2.0@gmail.com"
        }

        payload = {
        "from": {
            "postal_code": "63260000"
        },
        "to": {
            "postal_code": self.cep
        },
        "packages": [
            {
                "width": 11,
                "height": 17,
                "length": 11,
                "weight": 0.3,
                "insurance": 10.1
            },
            {
                "width": 20,
                "height": 25,
                "length": 25,
                "weight": 1.5,
                "insurance": 1000
            }
        ],
        "options": {
            "receipt": False,
            "own_hand": False
        },
        "services": "1,2,18"
        }

        response = requests.post(url, headers=headers, json=payload)

        

        return response.text
    def tempo_entrega_cep(self):
        pass

f = Frete("63260000")
print(f.calcular_valor_frete_por_cep())