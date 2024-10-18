import pandas as pd

arquivo = pd.read_excel("Realatorios\Pasta de trabalho.xlsx")
arquivo = arquivo.loc[:, "Aluno":"Situação"]

reprovados = arquivo[["Aluno", "Situação"]]
reprovados = reprovados[reprovados["Situação"]=="Reprovado"]
aprovados = arquivo[["Aluno", "Situação"]]
aprovados = aprovados[aprovados["Situação"]=="Aprovado"]
print(aprovados.count())


