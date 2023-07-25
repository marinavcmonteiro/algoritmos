qtde = int(input("Digite a quantidade de valores: "))

for i in range(1, qtde + 1):
    valor = int(input(f"Digite o valor {i}: "))
    fatorial = 1
    for j in range(1, valor + 1):
        fatorial *= j
    print(f"{valor}! = {fatorial}")
