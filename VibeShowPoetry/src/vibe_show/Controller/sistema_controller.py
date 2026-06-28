from view.menu import MenuView
from model.cad import Usuario

class SistemaController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def iniciar(self):
        while True:

            opcao = self.view.MenuPrincipal()   
            if opcao == '1':
                self.gerenciar_usuario()

            elif opcao == "2":
                print("Ver histórico de compras... (implementar na model/view)")
                
            elif opcao == "3":
                print("Comprar ingressos... (implementar na model/view)")
                
            elif opcao == "4":
                print("Escolher um local... (implementar na model/view)")
                
            elif opcao == "5":
                print("Solicitando reembolso... (implementar na model/view)")
                
            else:
                print("Opção inválida no Menu Principal.")


    def gerenciar_usuario(self):
        while True:
            opcao_user = self.view.MenuUsuario()
            if opcao_user == "1":

                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                self.model.cadastrar(nome, email, senha)


            elif opcao_user == "2":

                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                self.model.login(email, senha)

            elif opcao_user == "3":

                email = input("Digite seu email: ")

                self.model.recuperar_senha(email)

            elif opcao_user == "4":

                print("Voltando ao menu principal")
                break

            else:
                print("Opção inválida.")