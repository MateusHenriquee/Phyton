total_gasto = 0
mais_de_1000 = 0
menor_preco = 0
barato = ""
contador = 0

while True:
    produto = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço: R$ "))
    contador += 1
    total_gasto += preco

    if preco > 1000:
        mais_de_1000 += 1

    if contador == 1 or preco < menor_preco:
        menor_preco = preco
        barato = produto

    resposta = " "
    while resposta not in "SN":
        resposta = (
            str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        )

    if resposta == "N":
        break

print(f"\n{" FIM DO PROGRAMA ":-^40}")
print(f"a) O total gasto na compra foi de R$ {total_gasto:.2f}")
print(f"b) {mais_de_1000} produtos custam mais de R$ 1000.00")
print(f"c) O produto mais barato foi {barato}, que custou R$ {menor_preco:.2f}")
