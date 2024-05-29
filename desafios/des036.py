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
print(f"Para pagar uma casa de R${valor_casa:.2f} em {tempo_pagamento} anos,\na prestação será de {prestação:.2f}")
print()
if prestação <= (salario * 0.3):
    print("Seu emprétimo foi APROVADO!")
    print(f"O valor das prestações serão de {prestação:.2f} por mes por {tempo_pagamento} ano")
    print(f"Você terminará de pagar em {meses} meses")
else:
    print("Seu empréstimo foi REPROVADO")
    print(f"Pois a prestação fica mais que 30% do seu salário que seria: {porcentagem}")    