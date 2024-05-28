s = float(input("Digite seu salário para ganhar 15% de aumento: "))
a = s * 0.15
print(f"Seu salario aumentou de R${s:.2f} para: R${s+a:.2f}")
print(f"\033[4;32mAUMENTO DE R${a:.2f}\033[m")

# padrao = \033[m