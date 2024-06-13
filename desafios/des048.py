s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        s += c # isso é igual a "soma = soma + c"
        
    print(c, end=" ")
print(" ")
print(f"A soma dos {cont} valores é: {s}")