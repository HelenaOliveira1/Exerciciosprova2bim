print("Questão 23")
print("")

N = int(input("Digite um número: "))
aux = 1
p = 0
np = 0
while (aux < N):
  result = N / aux
  if (result == int(result)):
    print(aux)      
  aux += 1
  
print("Número de divisões executadas: ", aux)
   
    


