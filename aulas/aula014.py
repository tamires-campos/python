#UTILIZANDO FOR
for c in range(1, 10):
    print(c)
print("Fim")

#UTILIZANDO WHIE
c = 1
while c < 10:  #Enquanto C for menor de 10 
    print(c)   # irá mostrar valor de C
    c = c + 1  # irá somar mais 1 ao valor de C onde tbm posso escrever C+= 1
print("Fim")



##################################



for c in range (1, 5):
    v = int(input("Digite um valor: ")) #aqui irá digitar 4 vezes o valor
print("Fim")



n = 1 
while n != 0:
    n = int(input("Digite um valor: ")) # aqui irá digitar um valor até digitar o valor zero
    
    
 #################################
 
r = "S"
while r == "S":
    n = int(input("Digite um valor: "))    
    r = str(input("Quer continuar? [S/N]")).upper()  #aqui irá digitar valor até dizer q não quer continuar
print("Fim")



######################################


n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:               # aqui seria para não contabilizar o zero como número par
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print(f"Você digitou {par} números pares e {impar} números impares.")