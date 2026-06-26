class Usuario:
    usuarios_cadastrados = {}

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    @classmethod
    def cadastrar(cls, nome, email, senha):

        if email in cls.usuarios_cadastrados:
            print("Esse email já está cadastrado.")

        else:
            usuario = Usuario(nome, email, senha)
            cls.usuarios_cadastrados[email] = usuario
            print("Cadastro realizado com sucesso!")

    @classmethod
    def login(cls, email, senha):

        usuario = cls.usuarios_cadastrados.get(email)

        if usuario and usuario.senha == senha:
            print(f"Login efetuado com sucesso! Bem-vindo, {usuario.nome}.")

        else:
            print("Email ou senha incorretos.")

    @classmethod
    def recuperar_senha(cls, email):

        usuario = cls.usuarios_cadastrados.get(email)

        if usuario:
            print(f"A senha da conta é: {usuario.senha}")

        else:
            print("Email não encontrado.")

while True:

    print("\n1 - Cadastrar")
    print("2 - Login")
    print("3 - Recuperar senha")
    print("4 - Sair")

    opcao = input("Escolha uma das opções anteriores: ")

    if opcao == "1":

        nome = input("Digite seu nome: ")
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        Usuario.cadastrar(nome, email, senha)


    elif opcao == "2":

        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")

        Usuario.login(email, senha)

    elif opcao == "3":

        email = input("Digite seu email: ")

        Usuario.recuperar_senha(email)

    elif opcao == "4":

        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida.")