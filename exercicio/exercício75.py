brasileirao = ("Palmeiras", "Flamengo", "Athletico-PR", "Fluminense", "Red Bull Bragantino",
               "Bahia", "Botafogo", "Atlético-MG", "Corinthians", "Coritiba", "Cruzeiro",
               "São Paulo", "Vitória", "Santos", "Grêmio", "Internacional", "Vasco da Gama",
               "Clube do Remo", "Mirassol", "Chapecoense")

print(f'Os 5 primeiros classificados do brasileirão são: {brasileirao[0:5]}')

print(f'Os 4 últimos classificados do brasileirão são: {brasileirao[-4:]}')

print(f'Times em ordem alfabética: {sorted(brasileirao)}')

print(f'A Chapecoense está na {brasileirao.index("Chapecoense") + 1}ª posição')
