#Padrão de cor =  \033[m 
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print("\033[33mOs valores sorteados foram:\033[m ", end="")
for n in numeros:
    print(f"\033[32m{n}\033[m", end=" ")
print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")