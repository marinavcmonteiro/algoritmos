#Exercício 7
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0

voto = int(input(f"1 -> Candidato 1 \n"
                 f"2 -> Candidato 2 \n"
                 f"3 -> Candidato 3 \n"
                 f"4 -> Candidato 4 \n"
                 f"5 -> Voto nulo \n"
                 f"6 -> Voto em branco \n"
                 f"0 -> Sair \n"
                 f"Digite seu voto: "))

while voto != 0:
    if voto == 1:
        candidato1 += 1
    else:
        if voto == 2:
            candidato2 += 1
        else:
            if voto == 3:
                candidato3 += 1
            else:
                if voto == 4:
                    candidato4 += 1
                else:
                    if voto == 5:
                        nulo += 1
                    else:
                        if voto == 6:
                            branco += 1
    voto = int(input(f"1 -> Candidato 1 \n"
                    f"2 -> Candidato 2 \n"
                    f"3 -> Candidato 3 \n"
                    f"4 -> Candidato 4 \n"
                    f"5 -> Voto nulo \n"
                    f"6 -> Voto em branco \n"
                    f"0 -> Sair \n"
                    f"Digite seu voto: "))

print(f"Votos do candidato 1 = {candidato1}")
print(f"Votos do candidato 2 = {candidato2}")
print(f"Votos do candidato 3 = {candidato3}")
print(f"Votos do candidato 4 = {candidato4}")
print(f"Votos em branco = {branco}")
print(f"Votos nulos = {nulo}")
