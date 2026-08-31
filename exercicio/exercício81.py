numeros = []

while True:
    num = int(input("Digite um número: "))
    
    if num not in numeros:
        numeros.append(num)
        
    continuar = input("Quer continuar? [S/N] ").upper()
    if continuar == "N":
        break

numeros.sort()
print(f"Valores digitados: {numeros}")
