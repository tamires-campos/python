nome = input("Qual é o seu nome? ")
print(f"Prazer em te conhecer {nome:=^20}")

# :20 faz com que o nome seja escrito em 20 caracteres
# :>20 faz com que fique alinhado a direita
# :^20 faz com que fique centralizado
# :=^20 faz com fique centralizado dessa forma: =====Tamires=====


n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print(f"A soma é {s}, \n o produto é {m} e a divisão é {d}", end='')
print(f" Divisão inteira é {di} e a potência é {e}")


# end=''  é utilizado para não quebrar a linha
# \n  é utilizado para quebrar a linha