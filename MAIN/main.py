import tkinter as tk
from tkinter import messagebox, ttk
from database import criar_banco
from pandas_analysis import analisar_dados
from spark_analysis import analisar_dados_spark
from hadoop_storage import armazenar_dados_hadoop

class App:
    def __init__(self, root):
        # ...
        self.btn_analisar = tk.Button(self.root, text="Analisar Dados", command=self.analisar_dados)
        self.btn_analisar.grid(row=7, column=3, padx=10, pady=10)

        self.btn_analisar_spark = tk.Button(self.root, text="Analisar Dados com Spark", command=self.analisar_dados_spark)
        self.btn_analisar_spark.grid(row=8, column=3, padx=10, pady=10)

        self.btn_armazenar_hadoop = tk.Button(self.root, text="Armazenar Dados em Hadoop", command=self.armazenar_dados_hadoop)
        self.btn_armazenar_hadoop.grid(row=9, column=3, padx=10, pady=10)

    def analisar_dados(self):
        analisar_dados()

    def analisar_dados_spark(self):
        analisar_dados_spark()

    def armazenar_dados_hadoop(self):
        armazenar_dados_hadoop()

if __name__ == "__main__":
    criar_banco()
    root = tk.Tk()
    app = App(root)
    root.mainloop()