from datetime import date
atual = date.today().year
nascimento = int(input("Ano de nascimneto: "))
idade = atual - nascimento

print(f"O atleta tem {idade} anos")

if idade <=9:
    print("Sua classificação é MIRIM")
elif idade <=14:
    print("Sua classificação é INFANTIL")
elif idade <=19:
    print("Sua classificação é JUNIOR")
elif idade <=25:
    print("Sua classificação é SÊNIOR")
else:
    print("Sua classificação é MASTER")