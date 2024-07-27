num = list()
pares = list()
impares = list()
while True:
    while True:
        try:  #try e except são usados para manipulação de exceções. Eles permitem que você lide com erros de forma controlada e evite que seu programa pare de funcionar abruptamente.
            num.append(int(input("Digite um número: "))) # pela utilização do "int" obriga a digitação de um "número inteiro". Se o usuário digitar algo que não pode ser convertido para um inteiro (como letras ou caracteres especiais), um ValueError será levantado.
            break  # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print("\033[31mValor inválido! Por favor, digite um número inteiro.\033[m") # Código que será executado se o erro especificado ocorrer
            
    while True:   #loop para garantir que o usuário digite uma resposta válida (ou 'S' para continuar ou 'N' para parar) antes de prosseguir
        resp = input("\033[33mQuer continuar? [S/N] \033[m").strip().upper()  # Normaliza a entrada do usuário
        if resp in ('S', 'N'):
            break  # Sai do loop se a resposta for válida
        else:
            print("\033[31mResposta inválida! Por favor, digite 'S' para continuar ou 'N' para parar.\033[m")

    if resp == 'N':  # Verifica se o usuário quer parar
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print("-=" * 30)
print(f"A lista completa é {num}")
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")
