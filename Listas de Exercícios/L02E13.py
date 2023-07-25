#Exercício 13
ano_automovel = int(input("Digite o ano do modelo de automóvel: "))
peso_automovel = float(input("Dgite o peso do modelo de automóvel: "))

if ano_automovel <= 1970:
    if peso_automovel < 1200:
        print("Classe de peso: 1")
        print("Taxa de registro: 16,50")
    else:
        if peso_automovel <= 1700:
            print("Classe de peso: 2")
            print("Taxa de registro: 25,50")
        else:
            print("Classe de peso: 3")
            print("Taxa de registro: 46,50")
else:
    if ano_automovel < 1980:
        if peso_automovel < 1200:
            print("Classe de peso: 4")
            print("Taxa de registro: 27,00")
        else:
            if peso_automovel <= 1700:
                print("Classe de peso: 5")
                print("Taxa de registro: 30,50")
            else:
                print("Classe de peso: 6")
                print("Taxa de registro: 52,50")
    else:
        if peso_automovel < 1600:
            print("Classe de peso: 7")
            print("Taxa de registro: 19,50")
        else:
            peso_automovel <= 1600
            print("Classe de peso: 8")
            print("Taxa de registro: 55,50")
