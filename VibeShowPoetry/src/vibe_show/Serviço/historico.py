import random


class Pagamento:
    codigos_gerados = set()

    def __init__(self, nome, pago):
        self.nome = nome
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


class ConsultaIngresso:

    def verificar_compra(self, lista_compras, nome_usuario):

        for compra in lista_compras:

            if compra.nome == nome_usuario:

                print("Compra encontrada!")
                print(f"Código do ingresso: {compra.codigo}")
                return

        print("Nenhuma compra encontrada.")


compra1 = Pagamento("Ezequias", True)
compra1.get_codigo()

compra2 = Pagamento("Maria", True)
compra2.get_codigo()

compras = [compra1, compra2]

consulta = ConsultaIngresso()

nome = input("Digite seu nome: ")

consulta.verificar_compra(compras, nome)