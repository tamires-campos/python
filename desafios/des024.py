cid = str(input("Em que cidade você nasceu? ")).strip()
print(cid[:5].upper() == "SANTO")

"""aqui temos que pensar na hora da pessoa digitar. 
entao ela pode digitar com espaços no começo, por isso usamos o .strip() na primeira linha,
e também que poderia colocar letras maiusculas ou minusculas, por isso usamos .upper() para transformar tudo em maiusculo
e depois =="SANTO" em maiusculo para verificar"""