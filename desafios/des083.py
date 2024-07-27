expr = str(input("Digite a expressão: "))
pilha = []  # lista vazia
for simb in expr: #para cada um dos simbolas na expressão.
    if simb == "(": #se simbolo for igual a "("
        pilha.append("(")  #pilha irá receber "("
    elif simb == ")": #se for igual a ")"
        if len(pilha) > 0:  #verifica se pilha tem algum "("
            pilha.pop()   #remove o "("
        else:
            pilha.append(")")   #senao a pilha acrescenta ")"
            break  
if len(pilha) == 0:
    print("Sua expressão está válida")
else:
    print("Sua expressão está errada!")
