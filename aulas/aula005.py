# IMPORTANDO BIBLIOTECAS #

# import math -> irá importar a biblioteca inteira
# from math import sqrt -> irá importa somente a função "sqrt"

import math
num = int(input("Digite um número: "))
raiz = math.sqrt(num)
# aqui, assim que digitar math. -> irá aparecer toda a biblioteca que foi importada

print(f"A raiz de {num} é igual a {raiz}")

# poderia usar no lugar de raiz -> math.ceil(raiz)  para arredondar para cima
# ou math.floor(raiz)  para arredondar para baixo
# ou :.2f para mostrar apenas 2 casas após a virgula
