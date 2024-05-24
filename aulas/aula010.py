"""tempo = int(input("Qunatos anos tem seu carro/moto? "))
if tempo <=3:
    print("Veículo novo!")
else:
    print("Veículo velho, está na hora de trocar!")    
print("---FIM---")"""

# TAMBEM POSSO FAZER DA SEGUINTE MANEIRA:

tempo = int(input("Qunatos anos tem seu carro/moto? "))
print("Veículo novo" if tempo<=3 else "Veículo velho, está na hora de trocar!")
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
