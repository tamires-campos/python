distância = float(input("Qual é a distância da sua viagem? "))
print("=-=" *20)
print(f"Você está prestes a começar uma viagem de {distância}Km.")
print("=-=" *20)

# preço = distância * 0.5 if distância <= 200 else distância * 0.45
# print("E o preço da sua passagem será de R${preço:.2f}")

if distância <= 200:
    print(f"Sua passagem custará R${distância*0.5:.2f}")
else:
    print(f"Sua passagem custará R${distância*0.45:.2f}")