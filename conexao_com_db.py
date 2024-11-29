import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

cursor = connection.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS Receita_Federal")
cursor.execute("use Receita_Federal")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vitima (
        id INT AUTO_INCREMENT PRIMARY KEY,
        renda DECIMAL(10, 2) NOT NULL,
        cpf VARCHAR(14) NOT NULL UNIQUE,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255) NOT NULL,
        telefone VARCHAR(15) NOT NULL,
        tipo_pessoa ENUM('Física', 'Jurídica') NOT NULL
    );
''')

cursor.execute("show tables")

for tabela in cursor:
    print(tabela)
