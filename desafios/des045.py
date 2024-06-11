#Padrão de cor =  \033[m
from random import randint  #módulo random
from time import sleep 

itens = ("pedra", "papel", "Tesoura")  #pedra seria item = 0  papel = 1  e  tesoura = 2
computador = randint (0, 2) #módulo irá escolher entre 0, 1, e 2
print("\033[7;37mVamos jogar Pedra, Papel ou Tesoura!\033[m")
print('''Suas opções:
\033[32m[ 0 ]\033[m PEDRA
\033[32m[ 1 ]\033[m PAPEL
\033[32m[ 2 ]\033[m TESOURA''')

jogador = int(input('Qual é a sua jogada? '))
print("JO")
sleep(0.8)
print("KEN")
sleep(0.8)
print("PO!!!")
sleep(0.5)

print('\033[31m-=\033[m' * 10)
print(f"O Computador escolheu {itens[computador]}") #irá sortear pedra, papel ou tesousa através da lista com módulo randint
print(f'O Jogador escolheu {itens[jogador]}')
print('\033[31m-=\033[m' * 10)
print("")

if computador == 0: #computador jogou pedra
    if jogador == 0:
        print("\033[7;35mEMPATE!\033[m")
    elif jogador == 1:
        print("\033[32mPARABÉNS! VOCÊ VENCEU O COMPUTADOR!\033[m")
    elif jogador == 2:
        print("\033[41mCOMPUTADOR GANHOU!\033[m")
    else:
        print("Jogada Inválida!")
        
    
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print("\033[41mCOMPUTADOR GANHOU!\033[m")
    elif jogador == 1:
        print("\033[7;35mEMPATE!\033[m")
    elif jogador == 2:
        print("\033[32mPARABÉNS! VOCÊ VENCEU O COMPUTADOR!\033[m")
    else:
        print("Jogada Inválida!")
    
    
elif computador == 2: #computador jogou tesoura
    if jogador == 0:
        print("\033[32mPARABÉNS! VOCÊ VENCEU O COMPUTADOR!\033[m")
    elif jogador == 1:
        print("\033[41mCOMPUTADOR GANHOU!\033[m")
    elif jogador == 2:
        print("\033[7;35mEMPATE!\033[m")
    else:
        print("Jogada Inválida!")
        
