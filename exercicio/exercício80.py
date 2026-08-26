valores = []

for i in range(0, 5):
    num = float(input(f"Digite um valor para a posição {i}: "))
    valores.append(num)
print("-" * 40)
print(f"Você digitou os valores: {valores}")
maior_valor = max(valores)
print(f"O maior valor digitado foi {maior_valor} nas posições: ", end="")
for índice, valor in enumerate(valores):
    if valor == maior_valor:
        print(f"{índice}... ", end="")
print()
menor_valor = min(valores)
print(f"O menor valor digitado foi {menor_valor} nas posições: ", end="")
for índice, valor in enumerate(valores):
    if valor == menor_valor:
        print(f"{índice}... ", end="")
print()
