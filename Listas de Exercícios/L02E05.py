#Exercício 5
numero_inteiro = int(input("Digite um número inteiro: "))
if (numero_inteiro % 10 == 0):
    metade = numero_inteiro/2
    print(f"A metade do número digitado é: {metade}")
else:
    print("O número digitado náo termina com 0")
