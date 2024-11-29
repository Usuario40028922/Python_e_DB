import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Receita_Federal")
cursor.execute("use Receita_Federal")


cursor.execute("DROP TABLE vitima")
cursor.execute('''
    
    CREATE TABLE IF NOT EXISTS vitima (
        renda float NOT NULL,
        cpf INT(11) NOT NULL UNIQUE AUTO_INCREMENT PRIMAY KEY,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255) NOT NULL,
        telefone INT(9) NOT NULL,
        tipo_pessoa VARCHAR(8) NOT NULL
    );
''')

cursor.execute("show tables")

for tabela in cursor:
    print(tabela)
    

cursor.execute('''CREATE TABLE Impostos(

    vitima_renda FLOAT NOT NULL,
    vitima_cpf INT(11) NOT NULL,

)
''')
                 
