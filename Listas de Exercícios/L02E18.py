#Exercício 18
codigo = int(input("Digite o código de seleção: "))

if codigo < 1 or codigo > 3:
    print("Código inválido")
else:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número:  "))
    if codigo == 1:
        print(f"Soma = {numero1 + numero2}")
    else:
        if codigo == 2:
            print(f"Multiplicação = {numero1 * numero2}")
        else:
            if numero2 == 0:
                print("Não pode ter divisão por zero")
            else:
                print(f"Divisão = {numero1 / numero2}")
