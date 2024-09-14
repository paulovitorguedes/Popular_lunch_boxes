import sqlite3

def criar_banco():
    conexao = sqlite3.connect('marmitas.db')
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            forma_pagamento TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()