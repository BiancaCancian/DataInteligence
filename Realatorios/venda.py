# Script retona o pior e melhor vendedor com base na planilha

import pandas as pd

excel = pd.read_excel("Realatorios\Vendas.xlsx")

mes = input("Qual mês você quer analisar?")

analise = excel.sort_values(by=f'{mes}', ascending=False)

print(f'O melhor vendedor do mês de {mes} foi o(a) {analise.iloc[0,0]}')

analise = excel.sort_values(by=f'{mes}', ascending=True)

print(f'O pior vendedor do mês de {mes} foi o(a) {analise.iloc[0,0]}')