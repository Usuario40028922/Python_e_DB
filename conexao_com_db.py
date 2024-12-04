import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password=''
)

cursor = connection.cursor()

def ain(oque):
    cursor.execute(f"{oque}")
    
#ain("CREATE DATABASE IF NOT EXISTS Receita_Federal")
ain("USE Receita_Federal")
ain("DROP TABLE Vitima")
ain('''CREATE TABLE IF NOT EXISTS Vitima (
        renda double NOT NULL,
        cpf BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        tipo_pessoa VARCHAR(8) NOT NULL)
    ''')
#ain("ALTER TABLE Vitima AUTO_INCREMENT = 11111111111")
ain("INSERT INTO Vitima(renda, nome, endereco, telefone, tipo_pessoa) VALUES(0.5, 'Amogus', 'Rua de ninguém', '+55(22)3456-789', 'Jurídica')")
ain("SELECT * FROM Vitima")
ain('''

    CREATE TABLE IF NOT EXISTS Impostos(
    
        

    )

''')
for tabela in cursor:
    print(tabela)

cursor.close()
connection.close()
