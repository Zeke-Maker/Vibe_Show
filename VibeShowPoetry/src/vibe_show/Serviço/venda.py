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


quantidade = int(input("Quantos ingressos deseja comprar? "))

for i in range(quantidade):
    resposta = input(f"Pagamento do ingresso {i+1} foi realizado? (s/n): ")

    if resposta.lower() == "s":
        ingresso = Pagamento(True)
        print(f"Ingresso {i+1} confirmado!")
        print(f"Código: {ingresso.get_codigo()}\n")
    else:
        print(f"Ingresso {i+1} não foi pago.\n")