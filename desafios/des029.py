from playsound3 import playsound

vel = int(input("Qual a velocidade atual do carro? "))
multa = (vel-80) * 7

if vel > 80:
    print(f"MULTADO! Você excedeu o limite permitido que é de 80Km/h \n Você deve pagar uma multa de R${multa},00")
    playsound('C:/Users/tamir_mwwail1/Documents/Estudos/python/desafios/audio/peido.mp3')
else:
    print("OK! Tenha um bom dia.\n Dirija com Segurança!")
    
