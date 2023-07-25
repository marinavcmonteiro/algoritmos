#Exercício 16
codigo = int(input("Digite um código: "))

if codigo < 101 or codigo > 106:
    mensagem = "Código inválido"
else:
    if codigo == 101:
        mensagem = "Vendedor"
    else:
        if codigo == 102:
            mensagem = "Atendente"
        else:
            if codigo == 103:
                mensagem = "Auxiliar técnico"
            else:
                if codigo == 104:
                    mensagem = "Assistente"
                else:
                    if codigo == 105:
                        mensagem = "Coordenador de Grupo"
                    else:
                        mensagem = "Gerente"

print(mensagem)
