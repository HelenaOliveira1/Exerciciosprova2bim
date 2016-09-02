print("Questão 39")
print("")

numero = eval(input("Número do aluno: "))
altura = float(input("Altura do aluno: "))
MA = altura
ME = altura
numM = 0
numm = 0

for i in range (1, 11):
    if (altura > MA):
        MA = altura
        numM = numero
    elif (altura < ME):
        ME = altura
        numm = numero
    print("")
    if (i != 10):
        numero = eval(input("Número do aluno: "))
        altura = float(input("Altura do aluno: "))

print("Maior Aluno: ", numM, "-", MA, "centímetros.")
print("Menor Aluno: ", numm, "-", ME, "centímetros.")

    
        
