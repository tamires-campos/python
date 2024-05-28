from random import randint
from time import sleep

computador = randint(0, 5) # faz gerar um número sortido entre 0 e 5

print("\033[31m-=-"*20)
print("\033[32mVou pensar em um número entre 0 e 5. Tente adivinhar...")
print("\033[31m-=-\033[m"*20)
jogador = int(input("Em que número eu pensei? ")) # Jogador tenta adivinhar
print("PROCESSANDO...")
sleep(2)

if jogador == computador:
    print("\033[42mPARABENS, VOCÊ ACERTOU!\033[m")
else:
    print(f"\033[41mPERDEU!\033[m Eu pensei no número {computador} e não no {jogador}")
    
    
# padrao = \033[m