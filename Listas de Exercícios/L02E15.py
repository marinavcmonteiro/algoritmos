#Exercício 15
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
numero4 = float(input("Digite o quarto número: "))

if numero1 < numero2 and numero1 < numero3 and numero1 < numero4:
    print(numero1)
else:
    if numero2 < numero3 and numero2 < numero4:
        print(numero2)
    else:
        if numero3 < numero4:
            print(numero3)
        else:
            print(numero4)