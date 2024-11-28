import mysql.connector

# Conectar ao MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='exemplo_db'
)

cursor = conn.cursor()

# Inserir um registro
cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES ('Produto A', 10.50, 100)")
conn.commit()

# Inserir dois registros
produtos = [
    ('Produto B', 15.75, 200),
    ('Produto C', 7.25, 150)
]
cursor.executemany("INSERT INTO produtos (nome, preco, quantidade) VALUES (%s, %s, %s)", produtos)
conn.commit()

print("Dados inseridos com sucesso.")

# Fechar conexão
cursor.close()
conn.close()
