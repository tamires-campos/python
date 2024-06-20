totmulher20 = 0  # total de mulherres menores que 20 anos
maioridade = 0   # pessoas com mais de 18 anos
tothomens = 0    # total de homens
print("-" * 20)
print(f"{"CADASTRE UMA PESSOA":^20}")
print("-" * 20)
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":  # enquanto o sexo nao for M ou F ele irá aparecer novamente a pergunta
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if idade >= 18:
        maioridade += 1    
    if sexo == "M":
        tothomens += 1    
    if sexo == "F" and idade < 20:
        totmulher20 += 1    
    resp = " "
    while resp not in "SN": # enquanto a resp nao for S ou N ele irá perguntar novamente
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print(f"Existe {maioridade} maiores de 18 anos")
print(f"foram cadrastrados {tothomens} homens")
print(f"Ao todo são {totmulher20} mulheres com menos de 20 anos")

