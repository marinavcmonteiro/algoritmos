#Exercício 6
soma = 0
qtde = 0
numero = int(input("Digite um número: "))
while numero >= 0:
    soma += numero
    qtde += 1
    numero = int(input("Digite um número: "))

if qtde > 0:
    print(f"Média = {soma/qtde:.2f}")
    