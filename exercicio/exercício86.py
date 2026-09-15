# Lista principal para guardar todos os dados e listas auxiliares
pessoas = []
dado = []
maior_peso = menor_peso = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso (kg): ')))
    
    # Define o maior e menor peso com base na primeira pessoa cadastrada
    if len(pessoas) == 0:
        maior_peso = menor_peso = dado[1]
    else:
        if dado[1] > maior_peso:
            maior_peso = dado[1]
        if dado[1] < menor_peso:
            menor_peso = dado[1]
            
    # Guarda uma cópia dos dados na lista principal e limpa a auxiliar
    pessoas.append(dado[:])
    dado.clear()
    
    # Pergunta se o usuário deseja continuar
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break

print('-=' * 30)

# A) Quantas pessoas foram cadastradas
print(f'A) Ao todo, você cadastrou {len(pessoas)} pessoas.')

# B) Listagem com as pessoas mais pesadas
print(f'B) O maior peso foi de {maior_peso}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()

# C) Listagem com as pessoas mais leves
print(f'C) O menor peso foi de {menor_peso}kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
print()
