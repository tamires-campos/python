#Padrão de cor =  \033[m 

tabela_brasileirao_2024 = ("Flamengo", "Bahia", "Botafogo", "São Paulo", 
                           "Athletico-PR", "Red Bull Bragantino", "Palmeiras", 
                           "Internacional", "Cruzeiro", "Atlético-MG", "Fortaleza", 
                           "Juventude", "Grêmio", "Vasco", "Fluminense", 
                           "Criciúma", "Corinthians", "Atlético-GO", "Vitória", "Cuiabá")
print("-=" * 20)
print(f"\033[32mLista de times do brasileirão:\033[m {tabela_brasileirao_2024}")  #Também poderia colcoar "for t in tabela_brasileirao_2024:    print(t)" e me mostraria um time em cada linha
print("-=" * 20)
print(f"\033[33mOs 5 primeiros são\033[m {tabela_brasileirao_2024[0:5]}")
print("-=" * 20)
print(f"\033[33mOs 4 últimos são\033[m {tabela_brasileirao_2024[-4:]}")
print("-=" * 20)
print(f"\033[33m Times em ordem alfabética:\033[m  {sorted(tabela_brasileirao_2024)}")
print("-=" * 20)
print(f"O São Paulo está na {tabela_brasileirao_2024.index("São Paulo")+1}ª posição")