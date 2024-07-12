lista = []

for i in range(5):
    while True:
        try:
            numero = int(input("Digite um valor: "))
            break  # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print("\033[31mValor inválido! Por favor, digite um número inteiro.\033[m")  # Mensagem de erro para entradas inválidas

    # Se for o primeiro valor ou se o valor for maior que o último valor na lista
    if i == 0 or numero > lista[-1]:
        # Adiciona o valor ao final da lista
        lista.append(numero)
        print("Adicionado ao final da lista...")
    else:
        # Inicializa a variável posicao para encontrar a posição correta de inserção
        posicao = 0
        # Loop para encontrar a posição correta para inserir o número
        while posicao < len(lista):
            # Se o valor atual for menor ou igual ao valor na posição atual da lista
            if numero <= lista[posicao]:
                # Insere o valor na posição correta
                lista.insert(posicao, numero)
                print(f"Adicionado na posição {posicao} da lista")
                # Sai do loop após inserir o valor
                break
            # Incrementa a variável posicao para verificar a próxima posição
            posicao += 1

# Imprime uma linha de separação
print("-=" * 30)
# Exibe os valores digitados em ordem
print(f"Os valores digitados em ordem foram {lista}")