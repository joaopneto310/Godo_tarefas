import sqlite3
from databases.conexao import conectar_bd

def criar_banco_dados():
     #Criando a tabela de tarefas no banco de dados SQlITE3
    conexao,cursor = conectar_bd()
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS tarefas (
                   cod_tarefa INTEGER PRIMARY KEY AUTOINCREMENT,
                   tarefa TEXT,
                   status TEXT);

                   """)
    conexao.commit()#Salvando as alterações
    conexao.close() #fechando a conexão