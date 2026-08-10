
# # # valor = int(input("Que valor você quer sacar? R$ "))
# # # total = valor
# # # ced = 100  
# # # totalced = 0

# # # while True:
# # #     if total >= ced:
# # #         total -= ced
# # #         totalced += 1
# # #     else:
# # #         if totalced > 0:
# # #             print(f'Total de {totalced} cédulas de R$ {ced}')
# # #         if ced == 100:
# # #             ced = 50
# # #         elif ced == 50:
# # #             ced = 20
# # #         elif ced == 20:
# # #             ced = 2
# # #         totalced = 0
# # #         if total == 0:
# # #             break

# # multiplicacao = 1
# # cont = 0

# # while True:
# #     numero = int(input("Digite um número inteiro: "))
    
# #     cont += 1
# #     multiplicacao *= numero
    
# #     if numero == 757:
# #         break

# # print(f"Você digitou {cont} números.")
# # print(f"A multiplicação entre todos eles é: {multiplicacao}")

# fr = str(input('Digite uma frase: ')).strip().upper()

# quantidade_e = fr.count('E')

# ultima_posicao = fr.rfind('E') + 1

# print(f'A letra "E" aparece {quantidade_e} vezes na frase.')
# if quantidade_e > 0:
#     print(f'A última letra "E" apareceu na posição {ultima_posicao}.')
# else:
#     print('A letra "E" não aparece na frase.')

import random

bot = random.randint(0, 9)

print("vou pensar em um número entre 0 e 9. tente adivinhar")

jogador = int(input("em que número eu pensei? "))

if jogador == bot:
    print(f"vc ganhou, boa. o bot pensou no número {bot}.")
    print("o bot perdeu f")
else:
    print(f"vc errou, o bot pensou no número {bot} e não no {bot}.")
    print("o bot ganhou kkkkkkkkkk")
