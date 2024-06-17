#Padrão de cor =  \033[m
from time import sleep

n1 = int(input("\033[36mPrimeiro valor: \033[m"))
n2 = int(input("\033[36mSegundo valor: \033[m"))
opção = 0

while opção != 5:
    print('''\033[32m[1] SOMAR\033[m
\033[33m[2] MULTIPLICAR\033[m
\033[34m[3] MAIOR VALOR \033[m
\033[m[4] NOVOS NÚMEROS\033[m
\033[31m[5] SAIR DO PROGRAMA\033[m''')
    opção = int(input(">>>>> Qual é a sua opção? "))
    print("")
    if opção == 1:
        soma = n1 + n2
        print(f"\033[32mA soma entre {n1} + {n2} é {soma}\033[m")
    elif opção ==2:
        mult = n1 * n2
        print(f"\033[33mA multiplicação de {n1} X {n2} é de {mult}\033[m")
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f"\033[34mEntre {n1} e {n2} o maior valor é {maior}\033[m")
    elif opção == 4:
        print("Informe os números novamente: ")
        n1 = int(input("\033[36mPrimeiro valor: \033[m"))
        n2 = int(input("\033[36mSegundo valor: \033[m"))
    elif opção == 5:
        print("Finalizando...")
    else:
        print("\033[41mOpção inválida. Tente novamente\033[m")
    print("")
    print('=-=' *10)
    print("")
    sleep(2)
print("Fim do programa! Volte sempre!")
