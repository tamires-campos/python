# CORES NO TERMINAL  PADRÃO ANSI

# \033[ X m
#       X = STYLE ; TEXT ; BACK  
# \033[0;33;44m  -> CÓDIGO DE COR

'''    Estilos (STYLE)
          Código	Estilo
            0	        Reset / Padrão
            1	        Negrito / Brilhante
            2	        Opaco (Dim)
            4	        Sublinhado
            7	        Inverter texto/fundo'''
            
            
'''    🧵 Cores do Texto (TEXT)
        Código	  Cor (PT-BR)	   Cor (EN)
          30	  Preto/Cinza	    Grey
          31	  Vermelho	    Red
          32	  Verde	            Green
          33	  Amarelo	    Yellow
          34	  Azul	            Blue
          35	  Magenta	    Magenta
          36	  Ciano	            Cyan
          37	  Branco	    White'''
          
          
'''   🧱 Cores de Fundo (BACK)
        Código	Cor (PT-BR)	Cor (EN)
        40	Preto/Cinza	Grey
        41	Vermelho	Red
        42	Verde	        Green
        43	Amarelo	        Yellow
        44	Azul	        Blue
        45	Magenta	        Magenta
        46	Ciano	        Cyan
        47	Branco	        White  '''



#print("\033[7;33;46mOlá, mundo!\033[m")


nome = "Tamires"
cor = { "padrao": "\033[m",
        "vermelho": "\033[4;31m",
        "verde": "\033[4;32m",
        "amarelo": "\033[4;33m",
        "roxo": "\033[4;34m",
        "rosa": "\033[4;35m",
        "azul": "\033[4;36m"}

print(f"Olá! Muito prazer em te conhecer,\033[m {cor["azul"]}{nome}\033[m!!!!")






# USANDO COLORAMA
from colorama import Fore, Back, Style, init
                   #fonte, fundo, estilo
init() #Inicializa o colorama

print(Fore.RED + "Este texto é vermelho" + Style.RESET_ALL) # Style.RESET_ALL - resetar todos os estilos aplicados até aquele ponto
print(Back.GREEN + "Este texto tem fundo verde" + Style.RESET_ALL)
print(Style.BRIGHT + "Este texto é brilhante" + Style.RESET_ALL) 

# Combinando estilos
print(Fore.BLUE + Back.YELLOW + "Texto azul com fundo amarelo" + Style.RESET_ALL)