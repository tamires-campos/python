n = str(input("Digite seu nome completo: ")).strip().title()
nome = n.split()
print("="*25)
print("\033[1;42mMUITO PRAZER!\033[m")
print(f"Seu primeiro nome é: {nome [0]}")
print(f"Seu ultimo nome é: {nome[len(nome)-1]}")

# padrao = \033[m