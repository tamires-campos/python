valores = []
while True:
    
    while True:
        try:
            valores.append(int(input("Digite um valor: "))) # pela utilização do "int" obriga a digitação de um "número inteiro". Se o usuário digitar algo que não pode ser convertido para um inteiro (como letras ou caracteres especiais), um ValueError será levantado.
            break  # Sai do loop se a conversão for bem-sucedida
        except ValueError:
            print("\033[31mValor inválido! Por favor, digite um número inteiro.\033[m") # Código que será executado se o erro especificado ocorrer
            
            
    resp = str(input("Quer continuar? [S/N] "))