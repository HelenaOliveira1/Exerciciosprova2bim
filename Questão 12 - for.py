print("Questão 12 - for")
print("")

num = int(input("Digite um número para realização da tabuada: "))

if (num >= 1 and num <= 10):
    for var in range (1,11):
        mult = var*num
        print(num,"X",var,"=",mult)

else:
    print("Números Inválidos!")
