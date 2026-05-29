class Usuario:
    usuarios_cadastrados = {}

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.reembolso = False

    @classmethod
    def login(cls):

        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        usuario = cls.usuarios_cadastrados.get(email)

        if usuario and usuario.senha == senha:

            print(f"\nLogin efetuado com sucesso!")
            print(f"Bem-vindo, {usuario.nome}.")

            opcao = input("\nDeseja solicitar reembolso? (s/n): ")

            if opcao.lower() == "s":

                usuario.reembolso = True
                print("Reembolso solicitado com sucesso!")

            else:
                print("Nenhum reembolso solicitado.")

        else:
            print("Email ou senha incorretos.")

usuario1 = Usuario("Ezequias", "ezequias@gmail.com", "1234")

Usuario.usuarios_cadastrados[usuario1.email] = usuario1

Usuario.login()