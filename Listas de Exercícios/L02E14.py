#Exercício 14
nome_aluno = input("Digite o nome do aluno: ")
frequencia = int(input("Digite o número de faltas: "))

if frequencia > 15:
    print("Reprovado")
else:
    nota_prova1 = float(input("Digite a nota da primeira prova: "))
    nota_prova2 = float(input("Digite a nota da segunda prova: "))
    nota_trabalho = float(input("Digite a nota do trabalho: "))

    media = (3*nota_prova1 + 5*nota_prova2 + 2*nota_trabalho)/10
    if media > 6:
        print("Aprovado")
    else:
        print("Fará prova final")
