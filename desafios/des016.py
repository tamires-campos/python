#import random
# posso colocar tres aspas """""" para colocar como comentario


from math import floor, trunc

num = float(input("Digite um número: "))
print(f"O número {num} tem a parte inteira {trunc(num)}")

# no lugar de trunc eu também poderia usar o floor
# ou usar o int()
