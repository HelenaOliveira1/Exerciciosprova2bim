print("Questão 29 - while")
print("")

preco = 1.99
aux = 1
cont = 1

print("Loja Quase Dois - Tabela de Preços")
while (cont <= 50):
    print("                 ",aux,"- R$ %.2f" %preco)
    aux +=1
    preco += 1.99
    cont += 1
