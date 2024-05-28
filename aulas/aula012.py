# padrao = \033[m

#CONDIÇÃO SIMPLES
"""nome = str(input("Qual é o seu nome? "))
if nome == "Gustavo":
    print("\033[42mQue nome bonito!\033[m")
print(f"Tenha um bom dia, {nome}!")"""


#CONDIÇÃO COMPOSTA
"""nome = str(input("Qual é o seu nome? "))
if nome == "Gustavo":
    print("\033[42mQue nome bonito!\033[m")
else:
    print("\033[41mSeu nome é bem normal.\033[m")
print(f"Tenha um bom dia, {nome}!")"""


#ESTRUTURA CONDICIONAL ANINHADA
nome = str(input("Qual é o seu nome? "))
if nome == "Gustavo":
    print("\033[42mQue nome bonito!\033[m")
elif nome =="Pedro" or nome =="Maria" or nome == "João":
    print("\033[43mSeu nome é bem popular no Brasil.\033[m")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("\033[44mBelo nome feminino.\033[m")
else:
    print("\033[41mSeu nome é bem normal.\033[m")   # else é opcional 
print(f"Tenha um bom dia, {nome}!")