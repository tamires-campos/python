print("\033[33m-=\033[m" * 10)
print(">> Gerador de PA <<")
print("\033[33m-=\033[m" * 10)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão da PA: "))
termo = primeiro
cont = 1
total = 0
mais = 10    # mais recebe 10 termos, pois ele obrigatóriamente irá mostrar 10 termos e depois irá somar caso queira  
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, "-> ", end="")
        termo = termo + razão
        cont += 1
    print("Pausa")
    mais = int(input("Quantos termos você quer mostrar a mais? ")) 
print(f"Progressão finalizada com {total} termos mostrados")
