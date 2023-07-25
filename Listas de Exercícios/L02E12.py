#Exercício 12
tempo = float(input("Digite o tempo em que os fundos foram mantidos: "))
if tempo < 1:
    print("Taxa de Juros: 0.55")
else:
    if tempo < 2:
        print("Taxa de Juros: 0.65")
    else:
        if tempo < 3:
            print("Taxa de Juros: 0.75")
        else:
            if tempo < 4:
                print("Taxa de Juros: 0.85")
            else:
                if tempo < 5:
                    print("Taxa de Juros: 0.90")
                else:
                    print("Taxa de Juros: 0.95")