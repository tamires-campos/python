# int (inteiro)   1,  3,  5,  15.250,  -4  (SEM VIRGULA)
# float (real)   -1, 5, 15.561, 7.7 (COM VIRGULA)
# bool (verdadeiro ou falso) True or False
# str (texto)  "Olá, mundo!"  "tudo bem?"  "7.5"  " " 

n = float(input("Digite um valor: "))
print(n)
# aqui podemos ver que se eu digitar um valor como 8, ele me retornará como 8.0 , pois coloquei o tipo primitivo "float"


n = input("Digite algo: ")
print(n.isnumeric())
#esse .isnumeric() irá verificar se o que eu digitei é um número ou nao me retornando true ou false
# .isalpha()  - me fala se é letra
# .isalnum()  - me fala se é letra ou num
# .isupper()  - me fala se está somente com letras maiúsculas
