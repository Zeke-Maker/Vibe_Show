import customtkinter as ctk
import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1w3R5y7I9*6",
    database="Usuario"
)

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
            login.configure(text="Usuário não encontrado", text_color='green')

def abrir_cadastro():
    janela_cadastro = ctk.CTkToplevel()
    janela_cadastro.title("Cadastro")
    janela_cadastro.geometry("400x300")

    nome = ctk.CTkLabel(
        janela_cadastro,
        text="Tela de Cadastro" 
    )    



ctk.set_appearance_mode('dark')

app = ctk.CTk()
app.title('Entrar')
app.geometry('400x400')

LabelUsuario = ctk.CTkLabel(app, text='Usuário:')
LabelUsuario.pack(pady=10)
CampoUsuario = ctk.CTkEntry(app, placeholder_text='Digite seu nome de Usuário')
CampoUsuario.pack(pady='10')

LabelSenha = ctk.CTkLabel(app, text='Senha:')
LabelSenha.pack(pady=10)
CampoSenha = ctk.CTkEntry(app, placeholder_text='Digite sua Senha')
CampoSenha.pack(pady='10')

login = ctk.CTkLabel(app, text="")
login.pack(pady="10")

botao_login = ctk.CTkButton(app, text="Entrar", command=db)
botao_login.pack(pady=10)

link = ctk.CTkLabel(app, text="Não tem conta? Cadastre-se", text_color="blue", cursor="hand2")
link.pack()

link.bind("<Button-1>", lambda e: abrir_cadastro())



app.mainloop()
