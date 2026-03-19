import pandas as pd
import glob

arquivos = glob.glob("data/*.csv")

dfs = [pd.read_csv(arquivo) for arquivo in arquivos]

df_faturas = pd.concat(dfs)

df = pd.read_csv(arquivos, sep=";")

print(df_faturas['Categoria'].value_counts())

print(df_faturas['Data de Compra'].value_counts())

print(df_faturas.sort_values(by='Categoria', ascending=True))

print(df_faturas['Nome no Cartão'].value_counts())


