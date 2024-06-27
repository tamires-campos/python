palavras = ('aprender', 'programar', 'linguagem', 'python', 'curao', 'gratis', 'estudar', 'praticar', 
            'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f"\nNa palavra {p.upper()} temos: ", end="")
    for letra in p: #para cada letra de p
        if letra.lower() in "aáãâeéêiíoôu":  #se a letra tiver "aeiou"
            print(letra, end=" ") #irá escrever e dar um espaço