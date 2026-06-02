primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

decimo_termo = primeiro_termo + (10 - 1) * razao

print(f'Os 10 primeiros termos dessa PA são:')

for c in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{c}', end=' → ')
print('FIM')
