cor = {"padrao": "\033[m",
        "vermelho": "\033[4;31m",
        "verde": "\033[4;32m",
        "amarelo": "\033[4;33m",
        "roxo": "\033[4;34m",
        "rosa": "\033[4;35m",
        "azul": "\033[4;36m"}

nome = input("Qual é o seu nome? ")
print(f"Olá, \033[m {cor["vermelho"]}{nome}\033[m! Prazer em te conhecer!")

#também poderia simplesmente digitar:
# print("Olá, ", nome, "! Prazer em te conhecer!")



