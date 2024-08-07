valores = []
while True:
    
    while True:
        try:  #try e except são usados para manipulação de exceções. Eles permitem que você lide com erros de forma controlada e evite que seu programa pare de funcionar abruptamente.
            valores.append(int(input("Digite um valor: "))) # pela utilização do "int" obriga a digitação de um "número inteiro". Se o usuário digitar algo que não pode ser convertido para um inteiro (como letras ou caracteres especiais), um ValueError será levantado.
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
print("-=" * 30)
print(f"Você digitou {len(valores)} elementos")
valores.sort(reverse=True)  #colocar os valores em ordem decrescente
print(f"Os valores em ordem decrescente são {valores}")
if 5 in valores:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 NÃO foi encontrado na lista!")
    