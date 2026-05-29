import random

class Pagamento:
    codigos_gerados = set()

    def __init__(self, pago):
        self.pago = pago
        self.codigo = None

    def get_codigo(self):
        if self.pago and self.codigo is None:

            while True:
                novo_codigo = random.randint(1000, 9999)

                if novo_codigo not in Pagamento.codigos_gerados:
                    Pagamento.codigos_gerados.add(novo_codigo)
                    self.codigo = novo_codigo
                    break

        return self.codigo
        
cadeira1 = Pagamento(True)

codigo = cadeira1.get_codigo()

print(codigo)