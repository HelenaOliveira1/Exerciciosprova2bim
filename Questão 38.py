print("Questão 38")
print("")

print("Parte I - Salário inicial 1.000,00 - Salário Atual (2016)")
print("")

ano = 1996
salario = 1015
percentual = 0.015

while (ano <= 2016):
    ano += 1
    aumento = salario*percentual
    salario += aumento
    percentual = percentual*2

print("Salário Atual: ", salario)

("")
print("Parte II - Salário inicial fornecido pelo usuário - Salário Atual (2016)")
print("")

ano = 1996
salario = float(input("Digite seu salário inicial: "))
percentual = 0.015

while (ano <= 2016):
    ano += 1
    aumento = salario*percentual
    salario += aumento
    percentual = percentual*2

print("Salário Atual: ", salario)
