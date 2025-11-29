from pagamento import Pagamento
from datetime import date
from datetime import datetime

class Pagar_Vista(Pagamento):
    def __init__(self, forma_pagamento, status="Aguardando pagamento"):
        super().__init__(forma_pagamento, status)
        self.data_do_pagamento = date.today()

    def confirmar_pagamento(self):

        self.data_do_pagamento = date.today()
        self.data_do_pagamento = datetime.strftime("%d/%m/%Y")
