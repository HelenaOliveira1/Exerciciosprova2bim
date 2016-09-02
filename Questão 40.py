print("Questão 40")
print("")

codigo = int(input("Digite o Código da Cidade: "))
veiculos = int(input("Digite o número de veículos de passeio (em 1999): "))
acidentes = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))
MA = acidentes
ME = acidentes
soma = 0
soma2 = 0
aux = 1
ccm = codigo
cc = codigo

for i in range (1,6):
    if (acidentes >= MA):
        MA = acidentes
        ccm = codigo
    else:
        ME = acidentes
        cc = codigo
    soma += veiculos
    if (veiculos <= 2000):
        soma2 += acidentes
        aux += 1
    for a in range (1,5):
        print("")
        codigo = int(input("Digite o Código da Cidade: "))
        veiculos = int(input("Digite o número de veículos de passeio (em 1999): "))
        acidentes = int(input("Digite o número de acidentes de trânsito com vítimas (em 1999): "))

media = soma/ 5
media2 = soma2/ aux

print("")
print("Maior índice de acidentes de trânsito: ",MA, "na cidade",ccm)
print("Menor índice de acidentes de trânsito: ",ME, "na cidade",cc)
print("Media de veículos da Somatória de todas as cidades: ", media)
print("Media de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: ", media2)
    
