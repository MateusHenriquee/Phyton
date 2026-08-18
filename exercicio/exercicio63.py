primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo = primeiro
cont = 1

print("Os 10 primeiros termos da PA são:")

while cont <= 10:
    print(f"{termo} ", end="-> ")
    termo += razao
    cont += 1

print("FIM")
