#TUPLAS  - As tuplas são imutáveis

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') #Posso deixar sem parenteses se quiser, mas irá escrever com parenteses no terminal
'''print(lanche[-1])
lanche[1] = "refrigerante"  isse comant=do não pode ser executado por conta de que tuplas são imutáveis

('Hamburguer', 'Suco', 'Pizza', 'Pudim')
     [0]         [1]     [2]      [3]
     [-4]        [-3]    [-2]     [-1]'''



for comida in lanche:    #NÃO PRECISA DE POSIÇÃO
    print(f"Eu vou comer {comida}")
print("Comi pra caramba!")

'''OUTRO EXEMPLO COM O MESMO RESULTADO!
 for cont in range(0, len(lanche)): -> esse len(lanche) vai contabilizar 5, pois não começa contar do zero
      print(f"Eu vou comer {lanche[cont]} na posição {cont}")
print("Comi pra caramba!")'''

'''for pos, comida in enumerate(lanche):  
    print(f"Eu vou comer {comida} na posição {pos}")
print("Comi pra caramba!")'''




# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') 
# print(sorted(lanche))   ->  sorted = irá mostrar organizado em ordem alfabética







a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b  # 'b + a' é diferente de 'a + b'
print(c)   #irá mostrar (2, 5, 4, 5, 8, 1, 2)
#print(len(c)) = 7
#print(c.count(5)) = 2  que sig que o numero 5 apareceu 2 vezes
# (2, 5, 4, 5, 8, 1, 2)
#print(c.index(4)) -> em qual posição está o numero 4? ele sempre pega a primeira ocorrencia = 2
#print(c.index(2, 1)) -> em que posição esta o num 2 a partir da posição 1?  6







pessoa = ("Tamires", 24, "F", 65,88) #posso ter dados de tipos diferentes... letras e numero..
#del(pessoa) -> apagou da memória, ou seja, a tupla é imutável mas ainda posso apagar ela da memoria
print(pessoa)