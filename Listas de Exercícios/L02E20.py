#Exercício 20
valor1 = int(input("Digite o primeiro valor: "))
if valor1 < 1 or valor1 > 10:
    print("Número inválido")
else:
    valor2 = int(input("Digite o segundo valor: "))
    if valor2 < 1 or valor2 > 10:
        print("Número inválido")
    else:
        soma = valor1 + valor2
        if soma < 8:
            print(f"Média = {soma / 2}")
        else:
            if soma == 8:
                print(f"Multiplicação = {valor1 * valor2}")
            else:
                if valor1 > valor2:
                    print(f"Divisão = {valor1 / valor2}")
                else:
                    print(f"Divisão = {valor2 / valor1}")
