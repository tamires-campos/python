frase ='Curso em Vídeo Python'
print(frase[::2])

print(""" aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
      iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
      ooooooooooooooooooooooooooooooooooooooooooooo""")
#colocamos 3 aspas para aparecer o texto inteiro 

print(frase.count('o'))
print(frase.upper().count('O'))

print(len(frase))
print(len(frase.strip())) 
#coloque espaços na frase para realizar o de cima

print(frase.replace('Python','Android'))

dividido = frase.split()
print(dividido[0])

print(dividido[2][3]) 
#aqui ele pega a frase dividida e a palavra q está em [2] que seria "video" ele irá me mostrar a [3] letra