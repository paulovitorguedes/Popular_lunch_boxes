from pyspark.sql import SparkSession

def analisar_dados_spark():
    # Criar uma sessão Spark
    spark = SparkSession.builder.appName("Análise de Dados").getOrCreate()

    # Ler os dados do banco de dados
    df = spark.read.format("jdbc").option("url", "jdbc:sqlite:marmitas.db").option("query", "SELECT * FROM registros").load()

    # Realizar análises com Spark
    print("Resumo dos dados:")
    print(df.describe())

    # Contar o número de registros por forma de pagamento
    print("\nNúmero de registros por forma de pagamento:")
    print(df.groupBy("Pagamento").count().show())

    # Calcular o total arrecadado por forma de pagamento
    print("\nTotal arrecadado por forma de pagamento:")
    print(df.groupBy("Pagamento").agg({"Quantidade": "sum"}).show())