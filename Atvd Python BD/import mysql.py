import mysql.connector

# Conectar ao MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha'
)

cursor = conn.cursor()

# Criar base de dados
cursor.execute("CREATE DATABASE IF NOT EXISTS exemplo_db")
cursor.execute("USE exemplo_db")

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2),
    quantidade INT
)
""")

print("Base de dados e tabela criadas com sucesso.")

# Fechar conexão
cursor.close()
conn.close()
