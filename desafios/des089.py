#Padrão de cor =  \033[m
ficha = list()

while True:
    nome = str(input("Nome: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])   #[0] [1] [2]
    resp = str(input("\033[33mQuer continuar? [S/N] \033[m")).upper()
    if resp in "N":
        break
print("\033[32m=\033[m" * 50)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}') #O CÓDIGO EM AZUL É ALINHAMENTO
print("\033[32m=\033[m" * 50)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:8.1f}')
while True:
    print("=" * 50)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print("\033[43mFINALIZANDO...\033[m")
        break
    if opc <= len(ficha) - 1:
        print(f"Notas de {ficha[opc][0]} são {ficha[opc][1]}")
print("\033[43m<<< VOLTE SEMPRE >>>\033[m")
