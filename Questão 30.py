print("Questão 30")
print("")

preco = 0.18
aux = 1

print("Preço do pão: R$ 0.18")
print("Panificadora Pão de Ontem - Tabela de Preços")
for tabela in range (1,51):
    print(aux,"- R$ %.2f" %preco)
    aux +=1
    preco += 0.18
