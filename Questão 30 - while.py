print("Questão 30 - while")
print("")

preco = 0.18
aux = 1
cont = 1

print("Preço do pão: R$ 0.18")
print("Panificadora Pão de Ontem - Tabela de Preços")
while (cont <= 50):
    print("            ", aux,"- R$ %.2f" %preco)
    aux +=1
    preco += 0.18
    cont += 1
