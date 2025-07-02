frase ='Curso em Vídeo Python'
print(frase[::2]) #Essa linha está usando fatiamento de string com três parâmetros: [ início : fim : passo ]

#O primeiro parâmetro (início) está vazio, então começa do início da string.
#O segundo parâmetro (fim) está vazio, então vai até o final da string.
#O terceiro parâmetro é 2, ou seja, ele vai pulando de 2 em 2 caracteres.

#Índices:   0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
#Texto:     C u r s o   e m   V  í  d  e  o     P  y  t  h  o  n
#Pulando:   C   r   o   e        í     e           y     h     n  lembrando que ele considera os espaços vazios

print(""" aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
      oooooooooooooooooooooooooooooooooooooooooooo
      uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu""")
#colocamos 3 aspas para aparecer o texto inteiro 

print(frase.count('o')) #conta a quantidade de ocorrências da letro "o"
print(frase.upper().count('O')) #coloca a frase em Maiúsculas e conta a quantidade de "O"

print(len(frase)) #O len() retorna o comprimento da string, ou seja, quantos caracteres ela tem, incluindo os espaços.
print(len(frase.strip())) #remove os espaços em branco do início e do final da string (mas não os do meio).
#coloque espaços na frase para testar o strip

print(frase.replace('Python','Android')) #troca a palavra 'Python' por 'Android'

dividido = frase.split() #divide a string em palavras, usando os espaços em branco como separador padrão.
print(dividido[0]) #['Curso', 'em', 'Vídeo', 'Python']
                   #   [0]     [1]    [2]       [3]
                   
print(dividido[2][3]) #aqui ele pega [2] que seria "video" ele irá me mostrar a [3] (terceira) letra

