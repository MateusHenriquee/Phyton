numeros = []

print("Digite os números que deseja adicionar à lista.")
print("Para encerrar, digite qualquer letra ou caractere não numérico.\n")

while True:
    entrada = input("Digite um número: ").strip()

    try:
        numero = int(entrada)
        numeros.append(numero)
    except ValueError:
        
        print("\nLeitura encerrada!\n")
        break


quantidade = len(numeros)
print(f"a) Quantos números foram digitados: {quantidade}")

numeros_decrescente = sorted(numeros, reverse=True)
print(f"b) A lista de valores em ordem decrescente: {numeros_decrescente}")

if 5 in numeros:
    print("c) O valor 5 foi digitado na lista? Sim, o valor 5 está na lista.")
else:
    print("c) O valor 5 foi digitado na lista? Não, o valor 5 não foi encontrado.")
