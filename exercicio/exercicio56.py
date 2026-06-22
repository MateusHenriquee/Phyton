from datetime import date

# Obtém o ano atual do sistema
ano_atual = date.today().year

total_maiores = 0
total_menores = 0

# Loop para ler o ano de nascimento de 7 pessoas
for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = ano_atual - nasc
    
    # Verifica a maioridade (18 anos)
    if idade >= 18:
        total_maiores += 1
    else:
        total_menores += 1

# Exibe os resultados finais
print(f'\nAo todo tivemos {total_maiores} pessoas maiores de idade.')
print(f'E também tivemos {total_menores} pessoas menores de idade.')
