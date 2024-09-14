from pyhive import hive

def armazenar_dados_hadoop():
    # Criar uma conexão com o banco de dados Hadoop
    conexao = hive.connect(host="localhost", port=9083, username="username", password="password")

    # Criar um cursor
    cursor = conexao.cursor()

    # Ler os dados do banco de dados
    conexao_sqlite = sqlite3.connect('marmitas.db')
    cursor_sqlite = conexao_sqlite.cursor()
    cursor_sqlite.execute("SELECT * FROM registros")
    registros = cursor_sqlite.fetchall()
    conexao_sqlite.close()

    # Armazenar os dados no banco de dados Hadoop
    for registro in registros:
        cursor.execute("INSERT INTO marmitas (nome, telefone, quantidade, forma_pagamento) VALUES (?, ?, ?, ?)", 
                       (registro[1], registro[2], registro[3], registro[4]))

    # Fechar a conexão
    conexao.close()