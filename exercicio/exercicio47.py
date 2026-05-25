from time import sleep
import random
tentativa1 = str(input('''Jokenpô:
                       [1]Pedra:
                       [2]Papel:
                       [3]Tesoura:
                       escolha: '''))
maquina = random.randint(1,3)
print('Jo')
sleep(2)
print('ken')
sleep(3)
print('pô')
sleep(1)
if tentativa1 == '1' and maquina == 1:
    print('iala, empatou')
elif tentativa1 == '1' and maquina == 2:
    print('Você ganhou!')
elif tentativa1 == '1' and maquina == 3:
    print('Que pena, você perdeu')

elif tentativa1 == '2' and maquina == 1:
    print('Parabéns, você ganhou!')
elif tentativa1 == '2' and maquina == 2:
    print('iala, empatou!')
elif tentativa1 == '2' and maquina == 3:
    print('Que pena, você perdeu')
 
elif tentativa1 == '3' and maquina == 1:
    print('Que pena, você perdeu')
elif tentativa1 == '3' and maquina == 2:
    print('Você ganhou!')
elif tentativa1 == '3' and maquina == 3:
    print('iala, empatou')