#Exercício 8
ano_atual = int(input("Informe o ano atual: "))
ano_nascimento = int(input("Informe seu ano de nascimento: "))
idade = ano_atual - ano_nascimento
if idade < 0:
    print("Idade inválida")
else:
    if idade <= 3:
        print("Bebê")
    else:
        if idade <= 11:
            print("Crianca")
        else:
            if idade <= 17:
                print("Adolescente")
            else:
                if idade <= 64:
                    print("Adulta")
                else:
                    print("Idosa")