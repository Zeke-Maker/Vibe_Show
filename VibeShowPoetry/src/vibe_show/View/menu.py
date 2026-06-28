class MenuView:
    def MenuPrincipal(self):
        print(
            'Olá, seja bem vindo ao Vibe Show! Você pode realizar uma das seguintes ações:')
        print('1-Cadastrar usuario ou fazer login.')
        print('2-Ver histórico de comprar.')
        print('3-Comprar ingressos.')
        print('4-Escolher um local')
        print('5-Solicitar reembolso')

        return input('Então, o que deseja? ')

    def MenuUsuario(self):
        print('Essas são as ações disponiveis:')
        print("\n1 - Cadastrar")
        print("2 - Login")
        print("3 - Recuperar senha")
        print("4 - Sair")

        return input('selecione uma das opções: ')
    