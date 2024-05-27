from random import randint
from time import sleep

computador = randint(0, 5) # faz gerar um número sortido entre 0 e 5

print("-=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
jogador = int(input("Em que número eu pensei? ")) # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(2)

if jogador == computador:
    print("PARABENS, VOCÊ ACERTOU!")
else:
    print(f"PERDEU! Eu pensei no número {computador} e não no {jogador}")
    