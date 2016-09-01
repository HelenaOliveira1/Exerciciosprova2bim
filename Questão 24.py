print("Questão 24")
print("")

N = int(input("Qual a quantidade de notas? "))
print("")
nota = float(input("Digite a nota: "))
i = 0
aux = 0

for media in range (1,N+1):
    soma = nota + i
    i = nota
    aux +=1
    if (aux < N):
        nota = float(input("Digite a nota: "))

media = soma/N
    
print("")
print("A média das notas é", media)
