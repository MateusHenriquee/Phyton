fr = str(input('Digite uma frase: ')).strip().upper()

print(f'A letra A aparece {fr.count("A")} vezes na frase.')

print(f'A primeira letra A apareceu na posição {fr.find("A") + 1}')

print(f'A última letra A apareceu na posição {fr.rfind("A") + 1}')
