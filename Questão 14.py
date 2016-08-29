print("Questão 14")
print("")

num = int(input("Digite um número: "))
quant = 0
pares = 0
impar = 0

while (quant <= 9):
    if (num %  2 == 0):
        pares += 1
    else:
        impar += 1
    if (quant < 9):
        num = int(input("Digite um número: "))
    quant += 1

print("Quantidade de Números Pares =", pares)
print("Quantidade de Números ímpares =", impar)
        
