from random import randint
from time import sleep

sla = randint(0,5)

print("vou pensar em um número entre 0 e 5, tente adivinhar!")

pensano = int(input("o numero que vc acha que estou pensando é: "))
sleep(2)
if pensano == sla:
    print("PARABENS MANO!!! eu estava pensando no numero {}".format(sla))
    
else:
    print("KKKKKKKKKKK EU GANHEI SEU MERDA, o numero q eu tava pensando era {} e nao {}".format(sla,pensano))
    