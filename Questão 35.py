print("Questão 35")
print("")

numero = int(input("Digite um número: "))
print("")
aux = 1
p = 0
np = 0
print("Números existentes de 1 até", numero)
while (aux < numero):
  result = numero / aux
  if (result == int(result)):
    print(aux)      
  aux += 1
  
