print("=" * 30)
print(f"{"BANCO CEV":^30}")
print("=" * 30)
valor = int(input("Que valor você quer sacar? R$ "))
total = valor
céd = 200
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1 #irá ver quantas vezes consegue tirar 50 reais do total
    else:
        if totcéd > 0:
            print(f"Total de {totcéd} cédulas de R${céd}")
        if céd == 200:
            céd = 100
        elif céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1    
        totcéd = 0  #importante essa linha para zerar o totcéd senão continua com os valores da antiga céd
        if total == 0:
            break
print("=" * 30)
print("Volte sempre ao BANCO CEV! Tenha um ótimo dia!")