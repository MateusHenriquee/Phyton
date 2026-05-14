from datetime import date

ano_atual = date.today().year

nascimento = int(input('Ano de Nascimento: '))
idade = ano_atual - nascimento

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 20:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
