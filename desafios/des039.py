#Padrão de cor =  \033[m

from datetime import date    # nesta linha eu importei a data para nao precisar perguntar para o usuário.
ano_atual = date.today().year

nasc = int(input("Qual seu ano de nascimento? "))
idade = ano_atual - nasc

print(f"\033[7;37mQuem nasceu em {nasc} fez/fará {idade} anos em {ano_atual}\033[m")

if idade == 18:
    print("Você tem que se alistar \033[42mIMEDIATAMENTE\033[m")
elif idade == 17: #aqui eu coloquei uma variação de exatamente 1 ano para que a palavra "ano" fique no singular
    saldo = 18 - idade
    print(f"\033[32mfalta {saldo} ano para o alistamento.\033[m")
    ano = ano_atual + saldo
    print(f"Seu alistameto será em {ano}. Ano que vem, se prepare!")
elif idade < 17: #aqui já seria de 2 anos para mais entao ficará sempre no plural
    saldo = 18 - idade
    print(f"\033[32mfaltam {saldo} anos para o alistamento.\033[m")
    ano = ano_atual + saldo
    print(f"Seu alistameto será em {ano}")
    
elif idade == 19: #aqui eu coloquei uma variação de exatamente 1 ano para que a palavra "ano" fique no singular
    saldo = idade - 18
    print(f"\033[31mVocê já deveria ter se alistado há {saldo} ano\033[m")
    ano = ano_atual - saldo
    print("seu alistamento foi ano passado")
elif idade > 19: #aqui já seria de 2 anos para mais entao ficará sempre no plural
    saldo = idade - 18
    print(f"\033[31mVocê já deveria ter se alistado há {saldo} anos\033[m")
    ano = ano_atual - saldo
    print(f"Seu alistameto foi em {ano}")