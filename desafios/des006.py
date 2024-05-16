n = int(input("Digite um número: "))
print(f" O numero é: {n} \n Seu dobro é {n*2} \n Seu triplo é {n*3} \n E sua raiz quadrada é {pow(n, (1/2)):.2f}")

#pare a raiz quadrada que fica muito grande, podemos utilizar {:.2Ff} q sig 2 casa flotuantes depois da virgula

#outra m\neira de fazer a raiz quadrada seria, pow(n, (1/2)) ou manter n**(1/2)