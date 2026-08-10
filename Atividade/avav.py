
# valor = int(input("Que valor você quer sacar? R$ "))
# total = valor
# ced = 100  
# totalced = 0

# while True:
#     if total >= ced:
#         total -= ced
#         totalced += 1
#     else:
#         if totalced > 0:
#             print(f'Total de {totalced} cédulas de R$ {ced}')
#         if ced == 100:
#             ced = 50
#         elif ced == 50:
#             ced = 20
#         elif ced == 20:
#             ced = 2
#         totalced = 0
#         if total == 0:
#             break

multiplicacao = 1
cont = 0

while True:
    numero = int(input("Digite um número inteiro: "))
    
    cont += 1
    multiplicacao *= numero
    
    if numero == 757:
        break

print(f"Você digitou {cont} números.")
print(f"A multiplicação entre todos eles é: {multiplicacao}")
