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
