class Usuario:
    usuarios_cadastrados = {}

    def __init__(self, nome=None, email=None, senha=None):
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

