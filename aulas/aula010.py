#if e else em Python — são estruturas de decisão, ou seja, servem para o programa tomar decisões com base em alguma condição.
#  💡 Operadores comuns usados no if:
"""   Operador	     Significado
        ==	           Igual
        !=	           Diferente
        >	           Maior que
        <	           Menor que
        >=	           Maior ou igual
        <=	           Menor ou igual    """


"""tempo = int(input("Quantos anos tem seu carro/moto? "))
    if tempo <=3:
        print("Veículo novo!")
    else:
        print("Veículo velho, está na hora de trocar!")    
    print("---FIM---")"""

# TAMBEM POSSO FAZER DA SEGUINTE MANEIRA:

tempo = int(input("Quantos anos tem seu carro/moto? "))
print("Veículo novo" if tempo<=3 else "Veículo velho, está na hora de trocar! kkk")
print("---FIM---")




#####################################


n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

m = (n1 + n2) / 2
print(f"Sua média foi {m:.1f}")

#print("PARABENS" if m>=6 else "ESTUDE MAIS")
if m>=6.0:
    print("PARABÉNS!")
else:
    print("Pode melhorar na próxima...")
