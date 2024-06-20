soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ""
totmulher20 = 0

cadastro = "CADASTRE UMA PESSOA"

while True:
    print("-" * 20)
    print(f"{cadastro:^20}")
    print("-" * 20)
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    soma_idade += idade
    
    quer = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if quer == "Nn":
        break
    
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
