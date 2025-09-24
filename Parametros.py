import pymysql
from datetime import date,datetime
import Conexao as Conectar
   
def pegar_parametro(parametro):
    # Conecta ao banco de dados
    
    conexao = Conectar.BancoDados_Dtv()
    cursor = conexao.cursor()
    cursor.execute("SET innodb_lock_wait_timeout = 60")
    try:	

        with conexao.cursor() as cursor:
            ConsultaSQL = f"SELECT `valor` FROM `pyparameter` WHERE `parametro`= '{parametro}'"
            cursor.execute(ConsultaSQL)
            results = cursor.fetchone()

            return results[0]
 

    finally:
        conexao.close()

   
def Atualizar_Parametro(parametro,novovalor):
    # Conecta ao banco de dados
    
    conexao = Conectar.BancoDados_Dtv()
    cursor = conexao.cursor()
    cursor.execute("SET innodb_lock_wait_timeout = 60")
    try:	

        with conexao.cursor() as cursor:
                    ConsultaSQL = f"UPDATE `pyparameter` SET valor = '{novovalor}' WHERE `parametro` = '{parametro}'"
                    cursor.execute(ConsultaSQL)
                    conexao.commit()
 

    finally:
        conexao.close()

