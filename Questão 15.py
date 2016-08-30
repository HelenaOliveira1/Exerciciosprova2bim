print("Questão 15")
print("")

#A série Fibonacci começa do número 1,
#e a sequência vai somando o seu número anterior com ele.
#No caso vai ter que printar dois números 1 , e  o próximo vai ser a soma desses dois (os anteriores)
#Então se eu tenho uma váriavel 1 com outra 1 e soma vou ter o proximo número da sequência
#Aí eu transformo a primeira variável no número anterior da sequência
#E transformo a segunda variável na soma
#E continuo somando até o n-ésimo
#Entendendo-se que o n-ésimo termo seria informado pelo usuário, e que ele é a quantidade de vezes que vai se repetir:

n = int(input("Informe o n-ésimo número da Sequência Fibonacci: "))
a = 1
b = 1
c = 0
auxiliar = 1
print(a)
print(a)
while (auxiliar <= n-2):
    c = a + b
    print(c)
    a = b
    b = c
    auxiliar += 1


