#DICIONÁRIOS
'''
tuplas () 
listas [] -> dados = list()
dicionários {} -> dados = dict()
'''

#FILME
#SRAE WARS     1977     GEORGE LUCAS
# título       ano        diretor       invés de identificar por [0][1][2]  agora possui um dicionario

filme = {
    'título': "Star Wars",
    'ano': 1977,
    'diretor': "George Lucas"
}

print(filme.values()) #retorna todos os valores do dicionario de "Filme"
print(filme.keys())   #retorna "titulo, ano e diretor"
print(filme.items())  #retorna todos os valores, 


for k, v in filme.items():
    print(f"O {k} é {v}") # "k" sig título e "v" sig o valor cadastrado em titulo 