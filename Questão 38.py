print("Questão 38")
print("")

print("Parte I - Salário inicial 1.000,00 - Salário Atual (2016)")
print("")

ano = 1995
salario = 1.015
percentual = 1.5

while (ano+2 <= 2016):
    aumento = salario*(percentual/100)
    salario += aumento
    percentual *= 2
    ano += 1

print("Salário atual: %.2f" %salario)

print("")
print("Parte II - Salário inicial informado pelo usuário - Salário Atual (2016)")
print("")

ano = 1995
salario = float(input("Digite o valor do salário inicial: "))
salario += 15
percentual = 1.5

while (ano+2 <= 2016):
    aumento = salario*(percentual/100)
    salario += aumento
    percentual *= 2
    ano += 1

print("Salário atual: %.2f" %salario)
