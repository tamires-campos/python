#Padrão de cor =  \033[m


n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
media = (n1 + n2) / 2

print(f"Tirando {n1} e {n2}, a média do aluno será de {media}")

if media >=7:
    print("O aluno está de \033[32mAPROVADO\033[m")
elif media >= 5 and media < 7: # tbm poderia escrever "elif 7> media >=5:"
    print("O aluno está de \033[7;37mRECUPERAÇÃO\033[m")
else:
    print("O aluno está de \033[31mREPROVADO\033[m")