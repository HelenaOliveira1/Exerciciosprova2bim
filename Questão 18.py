print("Questão 18")
print("")

N = int(input("Quantos números você quer que sejam comparados? "))
print("")
aux = 1
num = int(input("Digite um número: "))
MA = num
ME = num
soma = 0

while (aux <= N):
    if (aux < N):
        num = int(input("Digite um número: "))
    if (num > MA):
        MA = num
    elif (num < ME):
        ME = num
    soma = soma + num
    aux += 1

print("Maior número:", MA)
print("Menor número:", ME)
print("Soma igual a:", soma)
