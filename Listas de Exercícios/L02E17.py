#Exercício 17
codigo = int(input("Digite o código da unidade de disco: "))
if codigo < 1 or codigo > 4:
    resultado = "Código inválido"
else:
    if codigo == 1:
        resultado = "CD-ROM (700MB)"
    else:
        if codigo == 2:
            resultado = "DVD-ROM (4.7GB)"
        else:
            if codigo == 3:
                resultado = "DVD-9 (8.54 GB)"
            else:
                resultado = "Blu-Ray (25 GB)"

print(resultado)