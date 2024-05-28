nome = str(input("Digite seu nome completo: ")).strip() #essse strip() irá eliminar espaços no começo e no fim

print("\033[1;32;41mAnalisando seu nome...\033[m")
print(f"Seu nome em maiúsculas é {nome.upper()}")
print(f"Seu nome em minúsculas é {nome.lower()}")

# print(f"Seu nome tem ao todo {len(nome)-nome.count(" ")} letras")  # esse -nome.count(" ") irá contar espaços vazios e subtrair  da quantidade de caracteres 

separa = nome.split()
print(f"Seu primeiro nome é {separa[0]} e o mesmo contém {len(separa[0])} letras")

# padrao = \033[m