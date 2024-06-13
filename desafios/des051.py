#Padrão de cor =  \033[m

print("\033[31m=\033[m" * 10)
print("10 TERMOS DE UM PA")
print("\033[31m=\033[m" * 10)

primeiro = int(input("Primeiro Termo: "))
razão = int(input("Razão: "))
décimo = primeiro + (10 - 1) * razão

for c in range(primeiro, décimo + razão, razão):
    print(c, end=" -> ")
print("Fim")