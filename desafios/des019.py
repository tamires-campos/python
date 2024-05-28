from random import choice

n1 = input("Primeiro nome: ")
n2 = input("Segundo nome: ")
n3 = input("Terceiro nome: ")
n4 = input("Quarto nome: ")
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print(f"O aluno escolhido foi \033[1;32m{escolhido}\033[m")

# padrao = \033[m