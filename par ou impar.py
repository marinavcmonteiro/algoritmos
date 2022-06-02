# Aluno (a): Marina Vidal Coutinho Monteiro
# Curso: Engenharia de Software

from random import *

print("Para jogar deve-se escolher o número correspondente a sua jogada. \n0-Par \n1-Ímpar")
lance_jogador1 = int(input("Digite sua jogada, player 1: "))
if lance_jogador1 != 0 and lance_jogador1 != 1:
    print("Jogada Inválida")
else:
    if lance_jogador1 == 0:
        jogo = int(input("Deseja jogar contra o computador (opcao = 0) ou contra um ser humano (opcao = 1)? "))
        if jogo < 0 or jogo > 1:
            print("Jogo inválido")
        else:
            numero_escolhido1 = int(input("Digite um número inteiro positivo: "))
            if jogo == 0:
                numero_escolhido2 = int(randint(0, 10))
                print(f"Jogada player 2: {numero_escolhido2} ")
            else:
                numero_escolhido2 = int(input("Digite um número inteiro positivo: "))

            if numero_escolhido1 < 0 or numero_escolhido2 < 0:
                print("Jogada inválida")
            else:
                if numero_escolhido1 % 2 == 0 and numero_escolhido2 % 2 == 0:
                    vencedor = "Jogador 1"
                else:
                    if numero_escolhido1 % 2 == 0 and numero_escolhido2 % 2 != 0:
                        vencedor = "Jogador 2"
                    else:
                        if numero_escolhido1 % 2 != 0 and numero_escolhido2 % 2 == 0:
                            vencedor = "Jogador 2"
                        else:
                            numero_escolhido1 % 2 != 0 and numero_escolhido2 % 2 != 0
                            vencedor = "Jogador 1"
            print(vencedor)
    else:
        jogo = int(input("Deseja jogar contra o computador (opcao = 0) ou contra um ser humano (opcao = 1)? "))
        if jogo < 0 or jogo > 1:
            print("Jogo inválido")
        else:
            numero_escolhido1 = int(input("Digite um número inteiro positivo: "))
            if jogo == 0:
                numero_escolhido2 = int(randint(0, 10))
                print(f"Jogada player 2: {numero_escolhido2} ")
            else:
                numero_escolhido2 = int(input("Digite um número inteiro positivo: "))

            if numero_escolhido1 < 0 or numero_escolhido2 < 0:
                print("Jogada inválida")
            else:
                if numero_escolhido1 % 2 == 0 and numero_escolhido2 % 2 == 0:
                    vencedor = "Jogador 2"
                else:
                    if numero_escolhido1 % 2 == 0 and numero_escolhido2 % 2 != 0:
                        vencedor = "Jogador 1"
                    else:
                        if numero_escolhido1 % 2 != 0 and numero_escolhido2 % 2 == 0:
                            vencedor = "Jogador 1"
                        else:
                            numero_escolhido1 % 2 != 0 and numero_escolhido2 % 2 != 0
                            vencedor = "Jogador 2"
            print(vencedor)

