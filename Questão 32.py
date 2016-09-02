print("Questão 32")
print("")

num = int(input("Digite um número para o fatorial: "))
fatorial = 1
extra = num

while(num > 1):
    fatorial = fatorial*num
    num -= 1
    
print("Fatorial de:", extra )

for i in range (1, extra+1):
    print(extra)
    print("X")
    extra -= 1
    
print("=")
print(fatorial)


    
