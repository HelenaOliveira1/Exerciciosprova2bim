print("Questão 36")
print("")

num = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
termino = int(input("Terminar por: "))
mult = 0
print("")

if (comeco < termino):
    while (comeco <= termino):
        mult = comeco*num
        print(num, "X", comeco, "=", mult)
        comeco +=1
else:
    print("O número inicial é maior que o final!")
    print("Valores Inválidos!")


        

