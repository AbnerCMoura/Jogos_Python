import random;

def jogar():

    print("********************************")
    print("Bem-vindo ao jogo de Adivinhação ")
    print("********************************")


    numero_secreto = random.randrange(1,11) # Gera um número aleatório entre 1 e 10 (sem contar o 11) #
    tentativas = 0

    print("Digite a dificuldade: ")
    print("(1) Fácil, (2) Médio, (3) Difícil")
    nivel = int(input("Digite: "))
    pontos = 100

    if(nivel == 1):
        tentativas = 5
    elif(nivel == 2):
        tentativas = 4
    else:
        tentativas = 3

    for rodada in range(1, tentativas + 1):
        print(f"Tentativa:  {rodada} de {tentativas}") #interpolação de string com "f" no começo e {} definindo a var
        chute_str = input("Digite um número entre 1 e 10: ")
        chute = int(chute_str) # passando de string para inteiro

        if(chute < 1) or (chute > 10):
            print("Número deve ser entre 1 e 10!")
            continue

        if(numero_secreto == chute):
            print("Você acertou")
            print(f"Você marcou {pontos} pontos")
            break
        else:
            if(chute > numero_secreto):
                print("Número digitado é maior do que número secreto")
            elif(chute < numero_secreto):
                print("Número digitado é menor do que número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos



    print("Fim do jogo!")
    print(f"Numero digitado era: {numero_secreto}")

if(__name__ == "__main__"):
    jogar()