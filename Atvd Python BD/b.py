import mysql.connector

# Conectar ao MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='seu_usuario',
    password='sua_senha',
    database='exemplo_db'
)

cursor = conn.cursor()

# Consultar dados
cursor.execute("SELECT * FROM produtos")
resultados = cursor.fetchall()

if not resultados:
    print("Tabela vazia.")
else:
    print("Registros encontrados:")
    for linha in resultados:
        print(linha)

# Fechar conexão
cursor.close()
conn.close()
