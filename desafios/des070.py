print("-" * 30)
print(f"{"LOJA SUPER BARATÃO":^30}")
print("-" * 30)
total = totmil = menor = cont = 0
barato = " "
while True:
    produto = str(input("Nome do produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totmil +=1
    if cont == 1:  #se for o primeiro produto // tbm  poderia digitar # if cont == 1 or preco < menor:     e apagaria as linha q estão com #
        menor = preco
        barato = produto
    else:                      #
        if preco < menor:      #
            menor = preco      #
            barato = produto   #
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"{" FIM DO PROGRAMA ":-^40}")
print(f"O total da compra foi de R${total:.2f}")
print(f"Temos {totmil} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")