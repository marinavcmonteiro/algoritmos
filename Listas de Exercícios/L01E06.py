#Exercício 6
salario_bruto = float(input("Digite o valor do salário bruto: "))
valor_horaextra = float(input("Digite o valor da hora extra: "))
quantidade_horaextra = int(input("Digite a quantidade de horas extras: "))
salario_total = salario_bruto + valor_horaextra * quantidade_horaextra
salario_liquido = (1-0.08) * salario_total
print(f"O valor do salário líquido é: {salario_liquido} ")
