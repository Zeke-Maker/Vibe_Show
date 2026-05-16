import customtkinter as ctk
import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1w3R5y7I9*6",
    database="Usuario"
)

ctk.set_appearance_mode('dark')

janela = ctk.CTk()
janela.title('Cadastro')
janela.geometry('400x300')



janela.mainloop()