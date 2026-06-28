import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1w3r5y7i9*6",
        database="usuario"
    )

    return conexao 
    