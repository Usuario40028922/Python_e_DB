import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='aluno',
    auth_plugin='mysql_native_password'
)

cursor = connection.cursor()

def ain(oque):
    cursor.execute(f"{oque}")
    
ain("CREATE DATABASE IF NOT EXISTS Receita_Federal")
ain("USE Receita_Federal")

ain('''CREATE TABLE IF NOT EXISTS Vitima (
        renda double NOT NULL,
        cpf BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        endereco VARCHAR(255) NOT NULL,
        telefone VARCHAR(20) NOT NULL,
        tipo_pessoa VARCHAR(8) NOT NULL)
    ''')
ain("ALTER TABLE Vitima AUTO_INCREMENT = 11111111111")
ain("INSERT INTO Vitima(renda, nome, endereco, telefone, tipo_pessoa) VALUES(0.5, 'Amogus', 'Rua de ninguém', '+55(22)3456-789', 'Jurídica')")
ain("SELECT * FROM Vitima")
ain('''

    CREATE TABLE IF NOT EXISTS Impostos(
    vitima_renda double NOT NULL,
    vitima_cpf BIGINT NOT NULL,
    de_renda DOUBLE DEFAULT 0.05,
    inss DOUBLE DEFAULT 0.10,
    cofins DOUBLE DEFAULT 0.02,
    ipva DOUBLE DEFAULT 0.02,
    irpj DOUBLE DEFAULT 0.02,
    renda final double
    
    PRIMARY KEY(vitima_cpf),
    FOREIGN KEY(vitima_cpf) REFERENCES Vitima(cpf) ON DELETE ON UPDATE CASCADE,
    FOREIGN KEY(vitima_renda) REFERENCES Vitima(renda) ON DELETE ON UPDATE CACADE

    )

''')
ain("SELECT * FROM Vitima")
for tabela in cursor:
    print(tabela)
cursor.close()
connection.close()

