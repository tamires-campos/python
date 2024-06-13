#Padrão de cor =  \033[m

num = int(input("\033[mDigite um número: "))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[32m", end=" ")
        tot += 1
    else:
        print("\033[31m", end=" ")
    print(c, end=" ")
    
print(" ")
print(f"\033[mO numero {num} foi divisível {tot} vezes")

if tot == 2:
    print("\033[32mE por isso ele é PRIMO!!\033[m")
else:
    print("\033[31mE por isso ele NÃO É PRIMO!!\033[m")
    