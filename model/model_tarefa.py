import sqlite3
from databases.conexao import conectar_bd
from databases.create_database import criar_banco_dados

def inserir_tarefa(texto_tarefa):
    #icluindo na tabela tarefas
        conexao, cursor = conectar_bd()
        cursor.execute("""
                        INSERT INTO tarefas(tarefa, status)
                        VALUES (?, ?);
                       """, 
                       [texto_tarefa,"PENDENTE"] )
        conexao.commit()
        cod_tarefa = cursor.lastrowid
        conexao.close()
        return cod_tarefa
      


def recuperar_tarefas():
    conexao,cursor = conectar_bd()
    cursor.execute("""
                    SELECT * FROM tarefas;
                   """)
    tarefas = cursor.fetchall()
    conexao.close()


    return tarefas



def apagar_tarefas(codigo_tarefa):
    conexao,cursor = conectar_bd()
    cursor.execute("""
                      DELETE FROM tarefas;
                      WHERE cod_tarefa = ?;
                     """,
                     [codigo_tarefa])
    conexao.commit()
    conexao.close()
    
    