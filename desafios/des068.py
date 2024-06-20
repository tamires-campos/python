#Padrão de cor =  \033[m

from random import randint
v = 0
print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 15)

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0, 10) # computador joga numero entre 0 e 10
    total = jogador + computador
    tipo = ' '                 # nao pode esquecer desse espaço
    while tipo not in "PI":  #enquanto o tipo não estiver em "pPiI" ele irá ficar perguntando novamente
        tipo = str(input("Par ou Ímpar? [P/I]")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total foi de {total} ", end="")
    print("DEU PAR" if total % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("\033[32mVocê VENCEU!\033[m")
            v +=1
        else:
            print("\033[31mVocê PERDEU\033[m")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("\033[32mVocê VENCEU!\033[m")
            v += 1
        else:
            print("\033[31mVocê PERDEU\033[m")
            break
    print("\033[33mVamos jogar novamente...\033[m")
print(f"\033[31mGAME OVER!\033[m Você venceu {v} vezes.")


