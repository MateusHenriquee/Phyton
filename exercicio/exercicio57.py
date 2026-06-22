# Inicializamos as variáveis
maior_peso = 0
menor_peso = 0

for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    
    if p == 1:
        # Na primeira leitura, o peso é tanto o maior quanto o menor
        maior_peso = peso
        menor_peso = peso
    else:
        # Compara com os pesos já registrados
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'\nO maior peso lido foi de {maior_peso}kg')
print(f'O menor peso lido foi de {menor_peso}kg')
