#Padrão de cor =  \033[m

print(f'\033[1;35m{"  LOJAS TAMIRES  ":=^40}\033[m')  #COR ROSA
preço = float(input("preço das compras: R$"))

print('''\033[36mFORMAS DE PAGAMENTO:\033[m
\033[36m[ 1 ]\033[m à vista dinheiro/cheque
\033[36m[ 2 ]\033[m à vista cartão
\033[36m[ 3 ]\033[m 2x no cartão
\033[36m[ 4 ]\033[m 3x ou mais no cartão''')

opção = int(input("\033[36mQual a forma de pagamento? \033[m"))

if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2 
    print(f"\033[33mSua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS\033[m")
elif opção == 4:
    total = preço + (preço * 0.20)
    total_parc = int(input("Quantas parcelas? "))
    parcela = total / total_parc
    print(f"\033[33mSua compra será parcelada em {total_parc}x de R${parcela:.2f} COM JUROS\033[m")
else:
    total = preço
    print("\033[41mOPÇÃO INVÁLIDA DE PAGAMENTO.\033[m Tente novamente!")
    
print(f"Sua compra de \033[31mR${preço:.2f}\033[m vai custar \033[32mR${total:.2f}\033[m no final")



    