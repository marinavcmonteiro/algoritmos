#Exercício 1
quantidadeNegativos = 0
quantidadePositivos = 0
quantidadeZeros = 0
quantidade = int(input("Digite a quantidade de valores: "))
for i in range(1, quantidade + 1):
    valor = int(input(f"Digite o valor {i}: "))
    if valor < 0:
        quantidadeNegativos += 1
    else:
        if valor > 0:
            quantidadePositivos += 1
        else:
            quantidadeZeros += 1

print(f"Quantidade de negativos = {quantidadeNegativos}")
print(f"Quantidade de positivos = {quantidadePositivos}")
print(f"Quantidade de zeros = {quantidadeZeros}")
