num = int(input("Digite um número inteiro: "))
print('''escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input("Sua opção: "))

if opção == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}") # [2:] significa que peguei a partir do 3 número até o fim
elif opção == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}")
elif opção == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}")
else:
    print("opção inválida. Tente novamente.")
    