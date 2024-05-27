print("-=" * 20)
print("Analisador de triângulos")
print("-=" * 20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os segmento acima podem formar um Triângulo")
else:
    print("Os segmento acima NÃO PODEM formar um Triângulo")