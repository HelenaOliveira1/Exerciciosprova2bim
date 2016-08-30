print("Questão 17")
print("")

num = int(input("Digite um número para o fatorial: "))
fatorial = 1

while(num > 1):
    fatorial = fatorial*num
    num -= 1

print("O fatorial do número é:", fatorial)
