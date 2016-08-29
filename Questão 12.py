print("Questão 12")
print("")

num = int(input("Entre com o número para realização da tabuada: "))

if (num > 1 and num <= 10):
    var = 1
    mult = 0
    while (var <= 10):
        mult = num*var
        print (num , "X", var, "=", mult)
        var += 1

else:
    print("Números Inválidos!")
        


