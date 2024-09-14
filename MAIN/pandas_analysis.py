import pandas as pd

def analisar_dados():
    conexao = sqlite3.connect('marmitas.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM registros")
    registros = cursor.fetchall()
    conexao.close()

    # Criar um DataFrame com os dados
    df = pd.DataFrame(registros, columns=["ID", "Nome", "Telefone", "Quantidade", "Pagamento"])

    # Realizar análises básicas
    print("Resumo dos dados:")
    print(df.describe())

    # Contar o número de registros por forma de pagamento
    print("\nNúmero de registros por forma de pagamento:")
    print(df["Pagamento"].value_counts())

    # Calcular o total arrecadado por forma de pagamento
    print("\nTotal arrecadado por forma de pagamento:")
    print(df.groupby("Pagamento")["Quantidade"].sum() * 15)