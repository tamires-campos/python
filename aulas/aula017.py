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




'''PRÁTICA

num = (2, 5, 9, 1) #TUPLA
num[2] = 3  #numero na posição 2 (no caso  9) recebe 3  NÃO funciona por ser uma tupla

num = [2, 5, 9, 1] #LISTA
num[2] = 3   #funciona normalmente, pois é uma lista e então o numero 9 se torna 3
#num[4] = 7   # isso não funciona pois não tem posição 4
num.append(7) #aqui eu conseguiria adicionar o numero 7 a minha lista
num.sort  #coloca na ordem
num.sort(reverse=True)  #mostra ordem inversa
print(f"Essa lista tem {len(num)} elementos")  #mostrar quantidade de elementos
num.insert(2, 0)  # colocar na posição "2" o número "0" e empurra os demais pro lado
num.pop() #elimina o ultimo numero da lista
num.pop(2) #elimina o número da posição 2
num.remove(2) #elimina o primeiro numero 2 que aparecer e nao todos, mas se não tiver numero 2 ele costa erro
if 4 in num:
    num.remove(4)
else:
    print("Não achei o numero 4")
print(num)'''



'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f"{v}...", end=" ")
    
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
    
for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista.")'''




a = [2, 3, 4, 7]
#b = a    # quando exercutar "b[2] = 8"  ele alterará nas duas listas, pois estao vinculadas
b = a[:]  # aqui ele cria uma cópia individual e altera somente em b 
b[2] = 8  
print(f"Lista A: {a}")
print(f"Lista B: {b}")