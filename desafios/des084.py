#Padrão de cor =  \033[m

temp = []
princ = []
maior = menor = 0

while True:
    while True:
        try:
            nome = (input("Nome: "))
            if not nome.isalpha():
                raise ValueError("\033[31mO nome deve conter apenas letra.\033[m")
            temp.append(nome)
            break
        except ValueError as e:
            print(f"\033[31m{e}\033[m")  

    while True:
        try:
            temp.append(int(input("Peso: ")))
            break
        except ValueError:
            print("\033[31mValor inválido! Por favor, digite um número inteiro.\033[m")
            
    #verificando maior e menor peso
    if len(princ) == 0:
        maior = menor = temp[1] #esse [1] esta se referindo a segunda pergunta sobre o peso
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    
    princ.append(temp[:]) #é important criar lista dentro de outra para poder mostrar apenas um item da lista, por exemplo "print(princ[0] [1])"
    temp.clear() #sem o 'CLEAR' iria mostrar [['tata', 68], ['tata', 68, 'anne', 105], ['tata', 68, 'anne', 105, 'cris', 88]]
    
    while True:
        resp = input("\033[33mQuer continuar? [S/N] \033[m").strip().upper()
        if resp in ('S', 'N'):
            break  # Sai do loop se a resposta for válida
        else:
            print("\033[31mResposta inválida! Por favor, digite 'S' para continuar ou 'N' para parar.\033[m")
    
    if resp == 'N':
        break
print("\033[35m-=\033[m" * 30)
print(princ)
print(f"Ao todo, você cadastrou {len(princ)} pessoas.") #poderia criar um contador tbm
print(f"O maior peso foi de {maior}Kg. Peso de ", end="")
for p in princ:
    if p[1] == maior:
        print(f"[{p[0]}] ", end="")
print()
print(f"O menor peso foi de {menor}Kg. Peso de ,", end="")
for p in princ:
    if p[1] == menor:
        print(f"[{p[0]}] ", end="")
print()
