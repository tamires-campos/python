#VARIÁVEIS COMPOSTAS (LISTAS)

'''teste = list()
teste.append("Gustavo")
teste.append("40")
galera = list()
galera.append(teste[:])  #o mais importante é o "[:]" que faz criar uma cópia para se for alterado não irá alterar a cópia
teste[0] = 'Maria'
teste[1] = '22'
galera.append(teste[:])
print(galera)'''


'''galera = [['João', 19], ['Ana', 33], ["Joaquim", 13], ['Maria', 45]]
#print(galera) #irá mostrar a lista inteira
#print(galera[0]) # irá mostar só ['João', 19]
print(galera[0] [0]) #irá mostrar somente "João"'''


'''galera = [['João', 19], ['Ana', 33], ["Joaquim", 13], ['Maria', 45]]
for p in galera:
    #print(p) #irá criar cada nome e idade em uma linha
    #print(p[0]) #irá mostrar somente os nomes
    print(f"{p[0]} tem {p[1]} anos de idade.")'''
    
    
galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input("Nome: "))) #adiciona nome em lista "dado"
    dado.append(int(input("Idade: "))) #adiciona idade em lista "dado"
    galera.append(dado[:]) #faz uma cópia do conteudo da lista "dado" para a lista "galera". Sem essa cópia "[:]" ele gerará lista vazias 
    dado.clear()
    
for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmai += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmen += 1
        
print(f"Temos {totmai} maior(es) e {totmen} menor(es) de idade.")
        