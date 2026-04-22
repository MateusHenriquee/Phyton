nome_completo = str(input('Digite seu nome completo: ')).strip()
nomes = nome_completo.split()

print('Muito prazer em te conhecer!'.format(nomes))
print('Seu primeiro nome é: {}'.format(nomes[0]))
print('Seu último nome é: {}'.format(nomes[-1]))
