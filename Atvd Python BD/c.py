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
    # Exibir na horizontal
    print("Resultados na horizontal:")
    for linha in resultados:
        print(linha)

    # Exibir na vertical
    print("\nResultados na vertical:")
    for linha in resultados:
        for coluna in linha:
            print(coluna)
        print("-----")  # Para separar os registros

# Fechar conexão
cursor.close()
conn.close()
