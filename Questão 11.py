print("Questão 11")
print("")

inicio = int(input("Entre com o valor de ínicio: "))
fim= eval(input("Entre com o valor do fim: "))
if (inicio <= fim):
    auxiliar = inicio+1
    soma = 0
    while (auxiliar < fim):
        print(auxiliar)
        soma= auxiliar + soma
        auxiliar +=1
else:
    print ("Valores Invalidos")

print("FIM...")
