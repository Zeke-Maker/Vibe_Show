import customtkinter as ctk
import mysql.connector

conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1w3R5y7I9*6",
        database="Usuario"
    )

ctk.set_appearance_mode('dark')

janela_principal = ctk.CTk()
janela_principal.title('Vibe Show')
janela_principal.geometry('500x500')


def redirect():
    global janela_entrar

    cursor = conexao.cursor()
    def db():
        usuario = CampoUsuario.get()
        senha = CampoSenha.get()
        cursor.execute(
            "SELECT * FROM login WHERE email = %s AND senha = %s",
            (usuario, senha)
)
        resultado = cursor.fetchone()

        if resultado:
            login.configure(text="Login executado com sucesso", text_color='green')
        else:
            login.configure(text="Usuário não encontrado", text_color='red')

    def abrir_cadastro():
        global janela_cadastro

        janela_cadastro = ctk.CTkToplevel()
        janela_cadastro.title("Cadastro")
        janela_cadastro.geometry("400x300")
        janela_entrar.withdraw()


    janela_entrar = ctk.CTkToplevel(janela_principal)
    janela_entrar.title("entrar")
    janela_entrar.geometry('400x400')
    janela_principal.withdraw()

    LabelUsuario = ctk.CTkLabel(janela_entrar, text='Usuário:')
    LabelUsuario.pack(pady=10)
    CampoUsuario = ctk.CTkEntry(janela_entrar, placeholder_text='Digite seu nome de Usuário')
    CampoUsuario.pack(pady='10')

    LabelSenha = ctk.CTkLabel(janela_entrar, text='Senha:')
    LabelSenha.pack(pady=10)
    CampoSenha = ctk.CTkEntry(janela_entrar, placeholder_text='Digite sua Senha')
    CampoSenha.pack(pady='10')

    login = ctk.CTkLabel(janela_entrar, text="")
    login.pack(pady="10")

    botao_login = ctk.CTkButton(janela_entrar, text="Entrar", command=db)
    botao_login.pack(pady=10)

    link = ctk.CTkLabel(janela_entrar, text="Não tem conta? Cadastre-se", text_color="blue", cursor="hand2")
    link.pack()

    link.bind("<Button-1>", lambda e: abrir_cadastro())


botao_entrar = ctk.CTkButton(janela_principal, text='entre', command=redirect)
botao_entrar.pack(pady=10)

janela_principal.mainloop()