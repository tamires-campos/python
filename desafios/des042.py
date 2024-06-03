r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmento acima PODEM FORMAR um triângulo", end=" ") # esse end serve para o equilátero aparecer em seguida
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1: # != significa Diferança. E eu preciso fazer para todas as possibilidades
        print("ESCALENO!")
    else: 
        print("ISÓCELES!")
else:
    print("Os segmento acima NÃO PODEM FORMAR um triângulo!")