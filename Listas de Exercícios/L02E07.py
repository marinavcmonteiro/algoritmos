#Exercício 7
salario_atual = float(input("Digite o salário atual: "))
tempo_servico= float(input("Digite o tempo de servico: "))
if tempo_servico <= 1:
    salario_reajustado = salario_atual * 1.1
    print(salario_reajustado)
else:
    salario_reajustado = salario_atual * 1.2
    print(salario_reajustado)

#Exercício 7_correcao
salario_atual = float(input("Digite o salário atual: "))
tempo_servico = float(input("Digite o tempo de servico: "))

if tempo_servico <= 1:
    percentual = 1.1
else:
    percentual = 1.2
print(f"Salário novo = {salario_atual * percentual: .2f}")