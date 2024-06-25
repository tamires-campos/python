cont = ("Zero", "Um", "Dois", "Três", "Quatro", 
        "Cinco", "Seis", "Sete", "Oito", "Nove",
        "Dez", "Onze", "Doze", "Treze", "Catorze", 
        "Quinze", "Dezesseis", "Dezessete", "Dezoito", 
        "Dezeove", "Vinte")

while True:
    num = int(input("Digite um número entre 0 a 20: "))
    if 0 <= num <=20:
        print(f"Você digitou o número {cont[num]}")
        resp = " " #nao pode esquecer de dar um espaço
        while resp not in "SN": # enquanto a resp nao for S ou N ele irá perguntar novamente
            resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]   
        if resp == "N":
            break
    print("Tente novamente. ", end="")
print(f"{"PROGRAMA FINALIZADO":^30}")