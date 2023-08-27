import random

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randint(1, 100)
    total_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas+1):  # O valor final fornecido para range() não está incluído no resultado, o que é importante lembrar ao definir os intervalos corretos para os seus loops.
        chute = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute)
        chute = int(chute)

        if(chute < 1 or chute > 100):
            print("Número Fora do Intervalo")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if acertou:
            print("Você acertou")
            break
        else:
            if maior:
                print("Vc errou! O seu chute foi maior do que o número secreto",end="\n\n")

            elif menor:
                print('Vc errou! O seu chute foi menor do que o número secreto',end="\n\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

            """ 
            Ela funcionará da seguinte maneira, o usuário começa o jogo com 1000 pontos, e a cada rodada que ele não acerta o número secreto, ele perderá pontos. Quanto mais distante for o chute, mais pontos o usuário irá perder. Por exemplo, se o número secreto for 40, e o usuário chutar 20, ele irá perder 20 pontos, 
            que corresponde à distância entre os valores.
            """


    print("Fim do Jogo. Número de Tentativas:{1}. O número é: {0} ".format(numero_secreto, rodada), end="\n\n")
    print("*********************************")
    print("|      Sua Pontuação: {}       |".format(pontos))
    print("*********************************")

if (__name__ == "__main__"):
    jogar()