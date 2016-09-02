print("Questão 34")
print("")

num = int(input("Digite um número: "))
aux = 1
p = 0
np = 0

for i in range (1, num+1):
    result = num / aux
    if (result == int(result)):
      p +=1
    else:
      np += 1
    aux += 1

if (p == 2):
    print("É primo!")
else:
    print("Não é primo!")
 	
