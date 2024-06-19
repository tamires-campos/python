#Padrão de cor =  \033[m

resp = "S"
soma = quantidade = media = maior = menor = 0
while resp in "Ss":
    num = int(input("\033[33mDigite um número: \033[m"))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num  
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("\033[31mQuer continuar?\033[m \033[32m[S/N]\033[m ")).upper().strip()[0]
media = soma / quantidade
print(f"Você digitou \033[32m{quantidade}\033[m números e a média entre eles foi de \033[32m{media:.2f}\033[m")
print(f"O maior valor doi \033[42m{maior}\033[m e o menor valor foi \033[42m{menor}\033[m")

    
    