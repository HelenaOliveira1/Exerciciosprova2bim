print("Questão 37")
print("")

alt = float(input("Altura: "))
talt = 0
tpeso = 0
MaiorP = 0
MaiorA = 0
MenorP = 0
MenorA = 0
auxa = 1
auxp = 1

while (alt != 0):
    talt += alt
    if (alt > MaiorA):
        MaiorA += alt
    else:
        MenorA += alt
    alt = float(input("Altura: "))
    mediaa = talt/auxa
    auxa += 1
    
peso = float(input("Peso: "))
    
while (peso != 0):
    tpeso += peso
    if (peso > MaiorP):
        MaiorP += peso
    else:
        MenorP += peso
    peso = float(input("Peso: "))
    mediap = tpeso/auxp
    auxp += 1
    
print("")
print("Mais Gordo: ", MaiorP)
print("Mais Magro: ", MenorP)
print("")
print("Mais Alto: ", MaiorA)
print("Mais Baixo: ", MenorA)
print("")
print("Média dos Pesos: ", mediap)
print("Média das Alturas: ", mediaa)

