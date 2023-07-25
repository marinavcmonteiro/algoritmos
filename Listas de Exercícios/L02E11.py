#Exercício 11
horas_trabalhadas = int(input("Digite o número de horas trabalhadas na semana: "))
if horas_trabalhadas <= 40:
    salario_semanal = horas_trabalhadas * 15
    print(f"O salário semanal é: {salario_semanal}")
else:
    salario_semanal = 600 + (horas_trabalhadas - 40) * 21
    print(f"O salário semanal é: {salario_semanal}")
