print("Questão 20")
print("")

vzs = int(input("Quantas vezes você quer calcular o fatorial? "))
print("")
num = int(input("Digite um número para o fatorial: "))
fatorial = 1

for i in range (vzs):
    if (num < 16):
        while(num > 1):
            fatorial = fatorial*num
            num -= 1
            
        print("O fatorial do número é:", fatorial)
        
    else:
        print("Número não suportado!")
        
    fatorial = 1
    if (i < (vzs - 1)):
        num = int(input("Digite um número para o fatorial: "))

