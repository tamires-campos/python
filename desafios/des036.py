#Padrão = \033[m

print("\033[1;31m-=\033[m" * 10)
print("\033[32mEMPRÉSTIMO BANCÁRIO!\033[m")
print("\033[1;31m-=\033[m" * 10)

valor_casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual seu salário atual? R$"))
tempo_pagamento = int(input("Em quantos anos irá pagar o empréstimo? "))
meses = tempo_pagamento * 12

prestação = valor_casa / meses
porcentagem = salario * 0.3


# 30% do salário = salário * 0,3

print()
print(f"Para pagar uma casa de \033[7;37mR${valor_casa:.2f} em {tempo_pagamento} anos, a prestação será de {prestação:.2f}\033[m")
print()
if prestação <= (salario * 0.3):
    print("\033[1;32mSeu emprétimo foi APROVADO!\033[m")
    print(f"O valor das prestações serão de {prestação:.2f} por mes por {tempo_pagamento} ano")
    print(f"Você terminará de pagar em {meses} meses")
else:
    print("\033[1;31mSeu empréstimo foi REPROVADO\033[m")
    print(f"Pois a prestação fica mais que 30% do seu salário que seria: {porcentagem}")    