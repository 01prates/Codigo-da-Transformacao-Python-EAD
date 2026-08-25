import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

# INSERT - Inserir cliente
cursor.execute(
    "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
    ("João Silva", "joao@email.com")
)

conexao.commit()

# SELECT - Consultar clientes
cursor.execute("SELECT * FROM Clientes")

clientes = cursor.fetchall()

print("\nCLIENTES:")
for cliente in clientes:
    print(cliente)

# UPDATE - Atualizar cliente
cursor.execute(
    "UPDATE Clientes SET email = ? WHERE id = ?",
    ("joao123@email.com", 1)
)

conexao.commit()

# DELETE - Deletar cliente
cursor.execute(
    "DELETE FROM Clientes WHERE id = ?",
    (1,)
)

conexao.commit()

print("\nOperações realizadas com sucesso!")

conexao.close()