import random

print("**********************************")
print("Bem vindo ao jogo de adivinhação!!")
print("**********************************")

#numero_secreto = round(random.random() * 100) #random gera um numero aleatorio entre 0.0 e 1.0
numero_secreto = random.randrange(1, 101) #range entre 1 e 100
total_de_tentativas = 0
pontos = 1000
#rodada = 1

print("Qual nível gostaria de jogar?")
print("(1) Fácil (2) Médio (3) Difícil")
nivel = int(input("Digite o nível desejado: "))

if (nivel == 1 ):
    total_de_tentativas = 15
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

#while(rodada <= total_de_tentativas):
for rodada in range(1, total_de_tentativas + 1):
    # print("Tentativa {0} de {1}".format(rodada, total_de_tentativas))
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue

    acerto = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if(acerto):
        print("Você acertou! Parabéns, você fez {} pontos.".format(pontos))
        break
    else:
        if(chute_maior):
            print("Você errou. Você chutou um número maior que o número secreto.")
        elif(chute_menor):
            print("Você errou. Você chutou um número menor que o número secreto.")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    #rodada = rodada + 1

print("Fim do jogo")