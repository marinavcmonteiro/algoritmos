#Exercício 10
salario = float(input("Digite o valor do salário: "))
valor_financiado = float(input("Digite o valor a ser financiado: "))

if valor_financiado <= 5 * salario:
    print("Financiamento Concedido")
else:
    print("Financiamento Negado")
