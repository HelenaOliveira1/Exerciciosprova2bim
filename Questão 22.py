print("Questão 22")
print("")

n = int(input("Digite um número: "))
aux = 1
while (aux <= n):
  result = n / aux
  if (result == int(result)):
    print("É divisível por", aux)     
  aux = aux + 1
    
print("")
print("OBS.: Quando o número é divísivel apenas por 1 e por ele mesmo É PRIMO")
