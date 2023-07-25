#Exercício 2
maior = 0
menor = 0

for i in range(1, 20):
    valor = int(input(f"Digite o valor {i}: "))
    if i == 1:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"Maior valor = {maior}")
print(f"Menor valor = {menor}")
