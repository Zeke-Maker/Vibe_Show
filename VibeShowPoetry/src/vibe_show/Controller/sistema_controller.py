from view.menu import MenuView
from model.cad import Usuario

class SistemaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def iniciar(self):
        while True:

            opcao = self.view.MenuPrincipal()   

            if opcao == "1":

                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                self.model.cadastrar(nome, email, senha)


            elif opcao == "2":

                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                self.model.login(email, senha)

            elif opcao == "3":

                email = input("Digite seu email: ")

                self.model.recuperar_senha(email)

            elif opcao == "4":

                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida.")