#Bibliotecas:
#mysql-connector-python
import mysql.connector



#Variáveis
mydb = mysql.connector.connect(host="localhost", user="root")
#dictionary = True, opcional
cursor = mydb.cursor(dictionary = True) 

#Funções
def oque_vc_quer_rappa():
  lista = ['1 - ']
  a = input("")
  lista[0]
  
  
def create_database(nome):
  cursor.execute("CREATE DATABASE IF NOT EXISTS {nome}")
  return "USE {nome};"



#Início do código:

print(mydb)

#cursor.execute("USE aula_db;")

#cursor.execute()

cursor.execute("SHOW DATABASES;")

for registro in cursor.fetchall():
  print(f"")  

mydb.close()
