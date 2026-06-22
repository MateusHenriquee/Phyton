soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    soma_idade += idade
    
    # Lógica para o homem mais velho
    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
        
    # Lógica para mulheres com mais de 20 anos
    if sexo == 'F' and idade > 20:
        tot_mulher_20 += 1

media_idade = soma_idade / 4

print('\n' + '='*30)
print(f'A média de idade do grupo é de {media_idade:.1} anos.')
if nome_velho:
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
else:
    print('Não foram registrados homens no grupo.')
print(f'Ao todo são {tot_mulher_20} mulheres com mais de 20 anos.')
