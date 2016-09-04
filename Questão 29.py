print("Questão 29")
print("")

preco = 1.99
aux = 1

print("Loja Quase Dois - Tabela de Preços")
for tabela in range (1,51):
    print("                 ",aux,"- R$ %.2f" %preco)
    aux +=1
    preco += 1.99
