soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ""
totmulher20 = 0

for p in range(1, 5):
    print(f"-----{p}ª PESSOA-----")
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade
    if p == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
        
media_idade = soma_idade / 4

print(f"A média de idade do grupo é de {media_idade} anos")
print(f"O home mais melho tem {maior_idade_homem} e se chama {nome_velho}")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos")
