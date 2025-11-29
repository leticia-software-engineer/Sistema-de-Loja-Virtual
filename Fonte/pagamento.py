import sqlite3
from datetime import date
class Pagamento():
    '''A classe pagamento registra as informações do pagamento como a forma do pagamente e o seu status e valida após ser confirmado.'''

    def __init__(self, forma_pagamento, status = "Aguardando pagamento"):
        
        self.forma_pagamento = str(forma_pagamento)
        self.status = status
        

