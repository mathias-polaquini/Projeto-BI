Business Intelligence - Relatório de Faturas de Cartões

## ETL
Os dados foram extraídos de arquivos CSV contendo informações de transações de cartão de crédito.

Durante a transformação, foram realizadas:
- Conversão de datas para formato adequado
- Tratamento de valores numéricos
- Padronização de categorias
- Criação de colunas como ano, mês e dia da semana

Os dados tratados foram utilizados para análise exploratória.

## PERGUNTAS DE NEGÓCIO:
1.Qual é o valor médio gasto por transação?

2.Quais são os dias da semana com maior volume de gastos?

3.Existe crescimento ou redução nos gastos ao longo do tempo?

4.Quais são as categorias com maior impacto no total gasto?

5.Qual é o ticket médio por categoria?

6.Qual categoria tem maior gasto total?

## Modelo Dimensional (Star Schema)
O projeto segue o conceito de modelo estrela, composto por:

- Tabela fato: contém os valores das transações (valor em R$)
- Dimensões: representam os contextos de análise

Principais dimensões utilizadas:
- Tempo (ano, mês, dia da semana)
- Categoria das transações

As análises foram realizadas agregando os valores da tabela fato pelas dimensões, utilizando operações de agrupamento.




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