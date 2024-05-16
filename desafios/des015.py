Dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Qual foi o total de km rodado? "))

pago = (Dias * 60) + (km * 0.15)

print(f"O total a pagar é de R${pago:.2f}")