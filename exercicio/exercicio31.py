from time import sleep
velocidade = float(input("Qual a velocidade atual do carro? "))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7
    sleep(2)
    print("MULTADO! Você excedeu o limite de 80km/h.")
    print("O valor da multa é de R${:.2f}.".format(multa))
else:
    print("Velocidade dentro do limite. Boa viagem seu inutil!")
