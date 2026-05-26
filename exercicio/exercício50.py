soma = 0
cont = 0


for n in range(1, 501):
    
    if n % 2 != 0 and n % 3 == 0:
        soma += n
        cont += 1

print(f"A soma de todos os {cont} valores encontrados é {soma}.")
