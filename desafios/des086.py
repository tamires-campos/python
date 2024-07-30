matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
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
    print()
    
    