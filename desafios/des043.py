#Padrão de cor =  \033[m

peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura? (m) "))
imc = peso / (altura ** 2)

print(f"\033[7;37mO IMC dessa pessoa é de {imc:.1f}\033[m")

if imc < 18.5:
    print("\033[36mAbaixo do peso\033[m") #cor azul
elif imc <= 25:
    print("\033[32mPeso ideal\033[m") #cor verde
elif imc <= 30:
    print("\033[33mSobre peso\033[m") #cor amarelo
elif imc <= 40:
    print("\033[31mObesidade\033[m") #cor vermelho
else:
    print("\033[7;31mObesidade móbida\033[m") #fundo vermelho
    