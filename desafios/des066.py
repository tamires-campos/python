cont = soma = num = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    soma += num
    cont += 1
print(f"foram digitados {cont} e a soma entre eles vale {soma}")


