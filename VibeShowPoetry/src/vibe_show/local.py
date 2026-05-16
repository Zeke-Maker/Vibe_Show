class Escolher_Assento:
    
    def __init__(self,):
        self.disponiveis = list(range(1, 101))
        self.ocupadas = []

    def vagas_totais(self):
        escolha = int(input(f"\nescolha uma vaga entre: {self.disponiveis}"))

        if escolha in self.disponiveis:
            self.disponiveis.remove(escolha)
            self.ocupadas.append(escolha)
            print(f"Vaga {escolha} cadastrada, agora restam as vagas {self.disponiveis}")

        else:
            print("Vaga não disponivel")
        
        

assentos = Escolher_Assento()

assentos.vagas_totais()

