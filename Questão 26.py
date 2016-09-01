print("Questão 26")
print("")

eleitores = int(input("Qual a quantidade total de eleitores? "))
candidato1 = 0
candidato2 = 0
candidato3 = 0
print("")

for votos in range(1, eleitores+1):
    votos = int(input("Digite seu voto: "))
    if (votos == 1):
        candidato1 += 1
    elif (votos == 2):
        candidato2 += 1
    elif (votos == 3):
        candidato3 += 1
    else:
        while (votos != 1 and votos != 2 and votos != 3):
            print("")
            print("Voto Inválido")
            print("Repita")
            votos = int(input("Digite seu voto: "))
        
print("1° Candidato: ", candidato1)
print("2° Candidato: ", candidato2)
print("3° Candidato: ", candidato3)

if (candidato1 > candidato2 > candidato3):
    print("Candidato 1 Venceu!")
elif (candidato2 > candidato1 > candidato3):
    print("Candidato 2 Venceu!")
elif (candidato3 > candidato2 > candidato1):
    print("Candidato 3 Venceu!")
else:
    ("Empate!")
    

    
