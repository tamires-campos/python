'''
#Padrão de cor =  \033[m

numeros = list()
while True:
    n = int(input("Digite um valor: "))
    if n not in numeros:
        numeros.append(n)
        print("\033[32mValor adicionado com sucesso!\033[m")
    else:
        print("\033[31mValor já inserido anteriormente! Não irei cadastrar...\033[m")   
    r = str(input("\033[33mQuer continuar? [S/N] \033[m"))
    if r in "Nn":
        break
print("-=" *30)
numeros.sort()  # deixará meus numeros em ordem
print(f"Você digitou os valores {numeros}")
'''





numeros = list()
while True:
    while True:
        try:
            n = int(input("Digite um valor: ")) # pela utilização do "int" obriga a digitação de um "número inteiro". Se o usuário digitar algo que não pode ser convertido para um inteiro (como letras ou caracteres especiais), um ValueError será levantado.
            break  # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print("\033[31mValor inválido! Por favor, digite um número inteiro.\033[m") # Código que será executado se o erro especificado ocorrer

    if n not in numeros:
        numeros.append(n)
        print("\033[32mValor adicionado com sucesso!\033[m")
    else:
        print("\033[31mValor já inserido anteriormente! Não irei cadastrar...\033[m")   
    
    while True:   #loop para garantir que o usuário digite uma resposta válida (ou 'S' para continuar ou 'N' para parar) antes de prosseguir
        r = input("\033[33mQuer continuar? [S/N] \033[m").strip().upper()  # Normaliza a entrada do usuário
        if r in ('S', 'N'):
            break  # Sai do loop se a resposta for válida
        else:
            print("\033[31mResposta inválida! Por favor, digite 'S' para continuar ou 'N' para parar.\033[m")

    if r == 'N':  # Verifica se o usuário quer parar
        break

print("-=" * 30)
numeros.sort()  # Deixa os números em ordem crescente
print(f"Você digitou os valores {numeros}")


# A estrutura try-except é uma maneira poderosa de lidar com erros em Python, tornando seus programas mais robustos e menos propensos a falhas inesperadas. Ela permite que você capture e trate erros de maneira controlada, fornecendo feedback apropriado ao usuário e garantindo que seu programa continue a executar corretamente.