print("Questão 16")
print("")

#Modificar a questão anterior para repetir até que o valor da série seja maior que 500

n = 1
a = 1
b = 1
print(n)

while (n < 500):
    print(n)
    n = a + b
    a = b
    b = n

print(n)
print("")
print("Encerrou...")
