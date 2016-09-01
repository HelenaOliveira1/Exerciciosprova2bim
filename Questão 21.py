print("Questão 21")
print("")

n = int(input("Digite um número: "))
aux = 1
while (aux <= n):
	result = n / aux
	if (result == int(result)):
		print(aux, "É primo")
	else:
		print(aux, "Não é primo")
	aux = aux + 1

print("")
print("OBS.: Se aparecer na tela a mensagem -É primo- apenas duas vezes, significa que o número é realmente primo, senão significa que ele não é primo")
