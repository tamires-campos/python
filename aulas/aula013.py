# ESTRUTURAS DE REPETIÇÃO FOR(ITERAÇÃO )

'''for c in range(1, 6): #de 1 a 6 ele irá executar 5 vezes, pois não considera o ultimo. Poderia colocar (0, 6) entao ele executaria 6 vezes,pois estaria contando des do 0
    print("Parabens!") #coloque (c) para fazer uma contagem
print("FIM")'''

#  se quiser contagem regrassiva teria que escrever range(6, 0, -1) esse -1 sig "tirar"
# se quiser ir pulando de 2 em 2 teria que escrever range(0, 7, 2) esse 2 vai pulando



'''n = int(input("Digite um número: "))
for c in range(0, n+1):
    print(c)
print("FIM")'''
    
    


'''i = int(input("Início: ")) #começa a contar a partir desse número
f = int(input("Fim: ")) #termina a contagem neste número
p = int(input("Passo: ")) #1 = normal  \  2 = pulando ...
for c in range(i, f+1, p):
    print(c)
print("FIM")'''




'''for c in range(0, 3):
    n = int(input("Digite um valor: ")) #irá perguntar 3x
print("FIM")
'''


 
s = 0 
for c in range(0, 4): #irá fazer 4x 
    n = int(input("Digite um valor: "))
    s = s + n  # também poderia escrever como "s +=n"
print(f"O somatório de todos os valores foi igual a {s}")