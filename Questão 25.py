print("Questão 25")
print("")

n = int(input("Número de pessoas: "))
aux = 0
print("")

for media in range(1,n+1):
    idade = int(input("Sua idade: "))
    soma = aux + idade
    aux = soma
    
media = soma/ n

if (media >= 0 and media <= 25):
    print("Turma Jovem!")
elif (media <= 60):
    print("Turma Adulta!")
elif (media > 60):
    print("Turma Idosa!")
    
