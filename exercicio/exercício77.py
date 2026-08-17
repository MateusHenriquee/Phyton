numeros = (
    int(input("Digite o 1º número: ")),
    int(input("Digite o 2º número: ")),
    int(input("Digite o 3º número: ")),
    int(input("Digite o 4º número: "))
)

print("-" * 30)
print(f"Você digitou os valores: {numeros}")

print(f"A) O valor 9 apareceu {numeros.count(9)} vez(es).")

if 3 in numeros:
    
    print(f"B) O primeiro valor 3 foi digitado na {numeros.index(3) + 1}ª posição.")
else:
    print("B) O valor 3 não foi digitado em nenhuma posição.")

print("C) Os números pares digitados foram: ", end="")
revelou_par = False

for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")
        revelou_par = True

if not revelou_par:
    print("Nenhum número par foi digitado.")
print()