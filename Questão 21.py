print("Questão 21")
print("")

N = int(input("Digite um número: "))
aux = 1
primo = 0
naoprimo = 0

while (aux < N+1):
    result = N / aux
    if (result == int(result)):
      primo +=1
    else:
      naoprimo += 1
    aux += 1

if (primo == 2):
    print("É primo!")
else:
    print("Não é primo!")
 	
