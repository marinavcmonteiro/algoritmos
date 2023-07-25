#Exercício 19
nota = float(input("Digite a nota: "))

if nota < 0 or nota > 10:
    print("Nota inválida")
else:
    if nota >= 9:
        print("Conceito A")
    else:
        if nota >= 7:
            print("Conceito B")
        else:
            if nota >= 5:
                print("Conceito C")
            else:
                print("Conceito D")
