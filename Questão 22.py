print("Questão 22")
print("")

n = int(input("Digite um número: "))
aux = 1
p = 0
np = 0
while (aux <= n):
  result = n / aux
  if (result == int(result)):
    print("É divisível por", aux)
    p += 1
  else:
    np += 1
  aux += 1
if (p == 2):
  print("")
  print("É primo!")
else:
  print("")
  print("Não é primo!")
    
