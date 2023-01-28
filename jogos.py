import forca
import adivinhacao

def escolhe_jogo():
    print("********************************")
    print("Escholha o jogo desejado:  ")
    print("********************************")

    print("(1) Forca, (2) Advinhação")
    jogo = int(input("Escolha"))

    if (jogo == 1):
        print("Jogo da forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogo de Advinhação")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()