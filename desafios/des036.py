#Padrão = \033[m

print("\033[1;31m-=\033[m" * 10)
print("\033[32mEMPRÉSTIMO BANCÁRIO!\033[m")
print("\033[1;31m-=\033[m" * 10)

valor_casa = float(input("Qual o valor da casa? "))
salario = float(input("Qual seu salário atual? R$"))
tempo_pagamento = int(input("Em quantos anos irá pagar o empréstimo? "))
meses = tempo_pagamento * 12

prestação = valor_casa / meses



# 30% = salário * 0,3

if prestação <= (salario * 0,3):
    print("Seu emprétimo foi APROVADO!")
    print(f"O valor das prestações serão de {prestação}")
    print(f"O tempo em meses que você pagará será de {meses} meses")
else:
    print("Seu empréstimo foi REPROVADO")    