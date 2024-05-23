num = int(input("Informe um número: "))

m = num // 1000 % 10 #aqui vamos ir dividindo e pegando somente o resultado inteiro ou sejo 1234//1000 =1,234  ->  a parte inteira disso é = 1  ->  e esse 1 vamos fazer 1%10 = 0,1  ->  onde ele irá pegar só o que restou depois da virgula
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10

print("="*25)
print(f"Analisando o número {num}")
print(f"Milhar: {m}")
print(f"Centena: {c}")
print(f"Dezena: {d}")
print(f"Unidade: {u}")