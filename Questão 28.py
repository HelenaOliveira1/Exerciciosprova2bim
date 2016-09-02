print("Questão 28")
print("")

cds = int(input("Digite a quantidade de CDs: "))
soma = 0
print("")

for valor in range(cds):
    valor = float(input("Digite o valor do CD: "))
    soma += valor

media = soma/cds
print("Valor total investido na coleção: ", soma)
print("Média de valor gasto em cada CD: ", media)

