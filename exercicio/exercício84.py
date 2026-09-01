valores = []
pares = []
impares = []

while True:
    num = int(input("Digite um número: "))
    valores.append(num)
    
    resp = input("Quer continuar? [S/N] ").strip().upper()
    if resp == 'N':
        break

for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print("-=" * 30)
print(f"A lista completa é: {valores}")
print(f"A lista de pares é: {pares}")
print(f"A lista de ímpares é: {impares}")
