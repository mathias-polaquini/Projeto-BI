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