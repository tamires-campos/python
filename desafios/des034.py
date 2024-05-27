salário = float(input("Qual o seu salário atual? "))

if salário <= 1250:
    novo = salário + (salário * 0.15) 
else:
    novo = salário + (salário * 0.10) 
    
print(f"Agora seu salário será de R${novo :.2f}")