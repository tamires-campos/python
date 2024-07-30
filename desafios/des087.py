matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = maior = soma_coluna = 0
for l in range(0, 3):  #LINHA
    for c in range(0, 3): #COLUNA
        while True:
            try:
                matriz[l][c] = (int(input(f"Digite um valor para [{l}, {c}]: ")))
                break
            except ValueError:
                print("\033[31mValor inválido! Por favor, digite um número inteiro.\033[m")
print("-=" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="") # :^5  -> faz com q mostre em 5 espaços centralizado
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
    print()
print("-=" * 30)
print(f"A soma dos valores pares é {soma_pares}")

for l in range(0, 3):
    soma_coluna += matriz[l][2]
print(f"A soma dos valroes da terceira coluna é {soma_coluna}")

for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f"O maior valor da segunda linha é {maior}")
