#Exercício 1, 2 e 3
nota = int(input("Digite a nota do aluno: "))
if nota < 0:
    print("NOTA INVÁLIDA")
else:
    if nota > 100:
        print("NOTA INVÁLIDA")
    else:
        if nota >= 60:
            print("APROVADO")
        else:
            print("REPROVADO")
