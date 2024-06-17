'''from math import factorial

n = int(input("Digite um número para calcular seu fatorial: "))
f = factorial(n)
print(f"O fatorial de {n} é {f}")'''



###########  outra maneira

n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1                     # aqui eu coloco meu fatorial com um número limpo 
print(f"Calculando {n}! ")
while c > 0:
    print(c, end="")
    print(" X " if c > 1 else " = ", end="")
    f = f * c            # tbm poderia escrever "f *= c"
    c -= 1
print(f)




################ utilizando FOR

n1 = int(input('Digite um Número para \nCalcular o Fatorial: '))
m = 1
for r in range(n1, 0, -1):
       m *= r
print('Calculando { }! \nO Fatorial de { } é { }'.format(n1, m))