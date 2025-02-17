import sqlite3 as sql

# Conectar ao banco de dados
con = sql.connect('db_web.db')
cur = con.cursor()

# Criar a tabela users com as colunas nome e detalhes
cur.execute('''
CREATE TABLE IF NOT EXISTS users (
    UID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOME TEXT NOT NULL,
    DETALHES TEXT NOT NULL
)
''')

# Confirmar as mudanças
con.commit()

# Fechar a conexão
con.close()