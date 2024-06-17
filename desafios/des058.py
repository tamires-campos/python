#Padrão de cor =  \033[m

from random import randint
computador = randint(0, 100)
print("\033[32mSou seu computador... Acabei de pensar em um número entre 0 e 100.")
print("Será que você consegue adivinhar qual foi? \033[m")
acertou = False  # está com false pq vc não acertou ainda
palpites = 0

while not acertou:
    jogador = int(input("Qual é seu palpite? "))
    palpites += 1  # aqui irá contabilizar quantos palpites o jogadou deu 
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais...Tente mais uma vez.")
        elif jogador > computador:
            print("Menos... tente mais uma vez.")
print(f"\033[42mAcertou com {palpites} tentativas. Parabéns!\033[m")
