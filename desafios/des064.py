num = 0    # num = cont = soma = 0
cont = 0
soma = 0

num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    cont += 1
    num = int(input("Digite um número [999 para parar]: "))
print(f"Você digitou {cont} números e a soma entre eles foi de {soma}") #poderia fazer "cont - 1" e "soma - 999"
