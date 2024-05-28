# CORES NO TERMINAL  PADRÃO ANSI

# \033[ X m
#       L>  X = STYLE ; TEXT ; BACK
# \033[0;33;44m  -> CÓDIGO DE COR

# STYLE ->  O = NONE   1 = BOLD   4 = UNDERLINE (sublinhar)   E   7 = inverter posições
# TEXTE ->  30 AO 37  -> 30=BRANCO  31=VERMELHO  32=VERDE  33=AMARELO  34=AZUL  35=MAGENTA  36=CIANO  37=CINZA
# BACK  ->  40 AO 47  -> 40=BRANCO  41=VERMELHO  42=VERDE  43=AMARELO  44=AZUL  45=MAGENTA  46=CIANO  47=CINZA

"""text              background
30      grey     cinza      40  cinza
31      red      vermelho   41  vermelho
32      green    verde      42  verde
33      yellow   amarelo    43  amarelo
34      roxo     purple     44  roxo
35      Magenta  Magenta    45  rosa
36      cyan     ciano      46  
37      white    branco     107""" 

#print("\033[7;33;46mOlá, mundo!\033[m")


nome = "Tamires"
cor = {"padrao": "\033[m",
        "vermelho": "\033[4;31m",
        "verde": "\033[4;32m",
        "amarelo": "\033[4;33m",
        "roxo": "\033[4;34m",
        "rosa": "\033[4;35m",
        "azul": "\033[4;36m"}

print(f"Olá! Muito prazer em te conhecer,\033[m {cor["azul"]}{nome}\033[m!!!!")