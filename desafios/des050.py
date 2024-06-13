s = 0
for c in range(1, 7):
    v = int(input(f"Digite o {c}º valor: "))
    if v % 2 == 0:
        s += v
print(f"a soma dos pares foi igual a {s}")
    