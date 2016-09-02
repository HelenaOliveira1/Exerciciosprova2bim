print("Questão 38")
print("")

print("Parte I - Salário inicial 1.000,00 - Salário Atual (2016)")
print("")

ano = 1995
salario = 1.000
percentual = 1.5

while (ano <= 2016):
    aumento = (salario*percentual)/100
    salario += aumento
    percentual *= 2
    ano += 1

print("Salário atual: %.2f" %salario)
