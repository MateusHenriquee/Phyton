from random import randint
lista = []
jogo = []

quant = int(input("quantos jogos deseja realizar: "))
tot= 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogo.append(lista[:])   
    lista.clear()
    tot += 1
    print(f"os números sorteados foram {jogo}")