print("Questão 27")
print("")

turmas = int(input("Quantidade de turmas: "))
soma = 0

for alunos in range(1, turmas+1):
    alunos = int(input("Quantidade de alunos na turma: "))
    if (alunos <= 40):
        soma = soma +  alunos
    else:
        print("Turma muito grande (máx. 40 alunos)")

media = soma/turmas
print("A média de alunos por turma é: ", media)
