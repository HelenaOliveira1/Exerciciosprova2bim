print("Questão 23")
print("")

i = int(input("Quantas temperaturas são? "))
print("")
aux = 1
temp = int(input("Digite a temperatura: "))
MA = temp
ME = temp
soma = 0

while (aux <= i):
    if (aux < i):
        temp = int(input("Digite a temperatura: "))
    if (temp > MA):
        MA = temp
    elif (temp < ME):
        ME = temp
    soma = soma + temp
    aux += 1
    
print("Maior temperatura:", MA)
print("Menor temperatura:", ME)
media = soma/i
print("Média: ", media)


