from random import randint
from termcolor import colored
import pyfiglet
texto = pyfiglet.figlet_format("Adivinhacao")
win = pyfiglet.figlet_format("Ganhou")

print(colored("JOGO DE ADIVINHAÇÃO!", "cyan"))
print(texto)
computador = randint(0,10)
print("-"*70)
print(colored("Olá, sou o seu computador! Acabei de pensar em um número entre 0 e 10", "blue"))
print(colored("Será que você consegue acertar?", "blue"))
print("-"*70)
acertou = False
palpites = 0 
while not acertou:
    jogador = int(input("Qual é o seu palpite?\n"))
    print("-"*25)
    palpites +=1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tesnte mais uma vez!")
        elif jogador > computador:
            print("Menos... Tente mais uma vez!")
print(colored(f"Acerou com {palpites} tentativas. Parabéns!.", "green"))
print(win)
