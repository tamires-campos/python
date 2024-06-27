'''TUPLAS ()
LISTAS []
DICIONÁRIO {}

lache = ['hamburgue', 'suco', 'pizza', 'pudim'] 
             [0]       [1]      [2]       [3]
lache[3] = 'picolé'  # irá substiuir o pudim

PARA ADICIONAR ELEMENTOS
lanche.append('cooki') #adiciona no final da lista
lanche.insert(0, 'cachorro-quente') #insere na posição zero e empurra os demais.

PARA DELETAR
dellanche[3]  # irá deletar a pizza
lanche.pop(3)  # irá deletar a pizza  massss normalmente se utiliza ".pop()" e deleta o ultimo elemento
lanche.remove('pizza')  #não utiliza indice, mas o valor que quer deletar, no caso pizza 

VERIFICANDO SE TENHO CONTEÚDO PARA REMOVE-LO
if 'pizza' in lanche:  #se tiver 'pizza' em lanche
    lanche.remove("pizza")  #remover pizza
    
valores = list(range(4, 11))  #poderia ir pulande de 2 em 2 com (4, 11, 2)
valores = 4   5   6   7   8   9  10
         [0] [1] [2] [3] [4] [5] [6]
         
         
valores = 8   2   5   4   9   3  0
para organizar é só utilizar "valores.sort()" -> 0 2 3 4 5 8 9
para organizar na ordem inversa é só utilizar "valores.sort(reverse=True)" -> 9 8 5 4 3 2 0
len(valores) ver quantos valores tem que nesse caso é = 7'''


PRÁTICA

num = (2, 5, 9, 1) #TUPLA
#num[2] = 3  #numero na posição 2 (no caso  9) recebe 3  NÃO funciona por ser uma tupla

num = [2, 5, 9, 1] #LISTA
num[2] = 3   #funciona normalmente 
