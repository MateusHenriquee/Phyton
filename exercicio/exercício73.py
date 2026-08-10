valor = int(input("Qual será o valor a ser sacado? R$ "))

cedulas = [100, 50, 5, 2]

print("\nCédulas entregues:")

for cedula in cedulas:
    quantidade = valor // cedula
    valor %= cedula              

    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R${cedula}")
