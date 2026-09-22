matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print("Digite os valores para preencher a matriz 3x3:")
for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f"Digite o valor para a posição [{linha}][{coluna}]: "))

print("\nMatriz resultante:")
for linha in range(3):
    for coluna in range(3):

        print(f"[{matriz[linha][coluna]:^5}]", end="")
    print()  
