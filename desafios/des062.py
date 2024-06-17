print("\033[33m-=\033[m" * 10)
print(">> Gerador de PA <<")
print("\033[33m-=\033[m" * 10)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1

while cont <= 10:
    print(termo, "-> ", end="")
    termo = termo + razão
    cont += 1
    
print("Fim")