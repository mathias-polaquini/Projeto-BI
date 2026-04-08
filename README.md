Business Intelligence - Relatório de Faturas de Cartões

PERGUNTAS DE NEGÓCIO:
1.Qual é o valor médio gasto por transação?

2.Quais são os dias da semana com maior volume de gastos?

3.Existe crescimento ou redução nos gastos ao longo do tempo?

4.Quais são as categorias com maior impacto no total gasto?

5.Qual é o ticket médio por categoria?

6.Qual categoria tem maior gasto total?



códigos anteriores para uma futura analise

import pandas as pd

# arquivos
arquivos = [
    "Fatura_2025-03-20"
]

# extract
dfs = [pd.read_csv(a, encoding="utf-8") for a in arquivos]

# juntar tudo
df = pd.concat(dfs, ignore_index=True)

# transform (exemplos)
df.columns = df.columns.str.lower().str.strip()

# exemplo: converter data
if "data" in df.columns:
    df["data"] = pd.to_datetime(df["data"], errors="coerce")

# exemplo: valores
if "valor" in df.columns:
    df["valor"] = df["valor"].astype(float)

# load
df.to_csv("fatura_tratada.csv", index=False)

print("ETL finalizado")