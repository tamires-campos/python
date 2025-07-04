cont = 1
while cont <= 10:                 # enquanto isso for verdade ele irá fazer a contição 
    print(cont, " -> ", end="")  # end=""  serve para continuar na mesma linha
    cont += 1
print("Acabou")



'''cont = 1
while True:                     # como já colocamos como verdade ele irá fazer sempre... só irá parar se tiver o comando break ou se interromper o programa 
    print(cont, " -> ", end="")  # end=""  serve para continuar na mesma linha
    cont += 1
print("Acabou")'''




n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break     #aqui o break interrompe e nao soma o 999 jogando o programa para o ultimo print 
    s += n
print(f"A soma vale {s}")

#lembrando como faz alinhamento 
'''nome = tamires
{nome:-^20} # irá alinhar tamires em 20 espaços '''