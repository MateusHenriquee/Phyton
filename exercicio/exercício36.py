salario = float(input('Qual é o salário do funcionário? R$ '))

if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento

# print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.'.format(salario,novo_salario))
# print('O valor do aumento foi de R$ {:.2f}.'.format(aumento))

# salario = float(input("Qual é o salário do funcionário?"))
# aumento15 = salario + (salario*0.15)
# aumento10 = salario + (salario*0.10)
# if salario > 1250:
#     print("Quem ganhava R${} passa a ganhar R${}".
# format(salario, aumento10))
# else:
#     print("Quem ganhava R${} passa a ganhar R${}".
# format(salario, aumento15))