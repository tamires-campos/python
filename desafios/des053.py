# PALÍNDROMO -> APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA BOLO, ANOTARAM A DATA DA MARATONA

frase = str(input("Digite uma frase: ")).strip().upper() # split elimina espaços antes e depois e upper deixa tudo em maiusculo
palavras = frase.split() # aqui ele separa em uma lista, por exem. CURSO, EM, VIDEO, DE, PYTHON
junto = "".join(palavras) # aqui ele junta tudo, por exem., CURSOEMVIDEODEPYTHON para eliminar os espaços
inverso = ""
for letra in range(len(junto) - 1, -1, -1): # fez o inverso
    inverso += junto[letra]                 # fez o inverso
if inverso == junto:
    print("TEMOS UM PALÍNDROMO")
else:
    print("A frase digitada não é um palíndromo!")
print(junto, inverso)




############## outra maneira ################# sem utilizar FOR

frase = str(input("Digite uma frase: ")).strip().upper() # split elimina espaços antes e depois e upper deixa tudo em maiusculo
palavras = frase.split() # aqui ele separa em uma lista, por exem. CURSO, EM, VIDEO, DE, PYTHON
junto = "".join(palavras) # aqui ele junta tudo, por exem., CURSOEMVIDEODEPYTHON para eliminar os espaços
inverso = junto[::-1]

if inverso == junto:
    print("TEMOS UM PALÍNDROMO")
else:
    print("A frase digitada não é um palíndromo!")
print(junto, inverso)