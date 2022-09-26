import adivinhacao
import forca

def escolhe_jogo():
	print("**********************************")
	print("*********Escolha seu jogo*********")
	print("**********************************")

	print("(1) Adivinhação (2) Forca")
	jogo = int(input("Escolha seu jogo: "))

	if(jogo == 1 ):
		print("Você escolheu o jogo de adivinhação")
		adivinhacao.jogar_adivinhacao()
	elif(jogo == 2):
		print("Você escolheu o jogo da forca")
		forca.jogar_forca()

if(__name__ == "__main__"):
	escolhe_jogo()