#Exercício 7
consumo = float(input("Digite o consumo de energia em quilowatt: "))
tarifa = float(input("Digite o valor da tarifa de energia elétrica: "))
ICMS = float(input("Digite a porcentagem do ICMS: "))
valor_consumo = consumo * tarifa
valor_imposto = (ICMS/100) * valor_consumo
valor_total = valor_consumo + valor_imposto
print(f"O valor a ser pago é: {valor_total}")
