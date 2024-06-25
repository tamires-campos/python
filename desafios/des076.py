listagem = ("Caderno", 15.90,
            "Caneta", 2.50,
            "Lápis", 1.20,
            "Borracha", 0.90,
            "Apontador", 1.50,
            "Mochila", 120.00,
            "Estojo", 25.00,
            "Régua", 3.00,
            "Tesoura", 7.00,
            "Cola", 4.50,
            "Marcador", 5.80,
            "Papel sulfite", 18.00,
            "Agenda", 20.00,
            "Corretivo", 6.30,
            "Transferidor", 2.80,
            "Compasso", 8.00,
            "Lápis de cor", 12.00,
            "Canetinhas", 14.50,
            "Pastas", 10.00,
            "Calculadora", 35.00)
print("-" * 40)
print(f"{"LISTAGEM DE PREÇOS":^40}")
print("-" * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end="")
    else:
        print(f"R${listagem[pos]:>6.2f}")
print("-" * 40)