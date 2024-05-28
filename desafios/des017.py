"""# PRIMEIRA MANEIRA
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = (co ** 2 + ca ** 2) ** (1/2)

print(f"A hipotenusa vai medir {hi:.2f}")"""


#SEGUNDA MANEIRA
from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
hi = hypot(co,ca)

print(f"A hipotenusa vai medir \033[1;31;43m{hi:.2f}\033[m")

# padrao = \033[m