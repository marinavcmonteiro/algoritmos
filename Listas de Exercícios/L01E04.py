#Exercício 4
salario_atual = float(input("Digite o salário atual: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento salarial: "))
valor_aumento = (porcentagem_aumento/100) * salario_atual
salario_aumento = salario_atual + valor_aumento
print(f"O valor do aumento é: {valor_aumento}")
print(f"O novo salário é: {salario_aumento}")