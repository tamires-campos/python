lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite um valor para a Posição {c}: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]     #MAIOR
        if lista[c] < menor:
            menor = lista[c]     #MENOR
print("=-" * 20)

print(f"Você digitou os valores {lista}")
print(f"O maior valor digitado foi {maior} na(s) posição(ões)", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}...", end="")
print()
print(f"O menor valor digitado foi {menor} na(s) posição(ões)", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}...", end="")
print()