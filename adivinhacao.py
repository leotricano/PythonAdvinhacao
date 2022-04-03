import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = (random.randrange(1, 51))
    total_de_tentativas = 0
    pontos=1000

    print("Qual nivel de dificuladade?")
    print("(1) Fácil (2) Médio (3) Díficil")

    nivel = int(input("Define o nível: "))

    if (nivel == 1):
        total_de_tentativas = 15
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range (1,total_de_tentativas +1):
        print(f"Tentativas {rodada} de {total_de_tentativas}")
        chute_str = input("digite um número entre 1 e 50: ")
        print("você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 50):
            print("Você deve digitar um número entre 1 e 50!")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print(f"parabéns! você fez {pontos} pontos.")
            break
        else:
           pontos_perdidos = abs(numero_secreto - chute)
           pontos = pontos - pontos_perdidos
           if (maior):
                print(f"Você errou! o seu chute foi maior que seu número secreto. Pontos:{pontos}.")
                if (rodada == total_de_tentativas):
                    print (f"O número secreto era {numero_secreto}. Você fez {pontos}")
           elif (menor):
                print(f"Você errou! o seu chute foi menor que seu número secreto. Pontos:{pontos}.")
                if (rodada == total_de_tentativas):
                    print (f"O número secreto era {numero_secreto}. Você fez {pontos}")

    print("fim do jogo")

if(__name__ == "__main__"):
    jogar()