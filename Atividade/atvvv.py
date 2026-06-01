
preco_normal = float(input("Digite o preço do produto: R$ "))

print("formas de pagamento: ")
print("[ 1 ] a vista dinheiro/cheque (15% de desconto)")
print("[ 2 ] a vista no cartão (8% de desconto)")
print("[ 3 ] em até 2x no cartão (Preço normal)")
print("[ 4 ] 3x ou mais no cartão (25% de juros)")

opcao = int(input("qual opção vc escolhe "))

if opcao == 1:
    total = preconormal * 0.85
elif opcao == 2:
    total = preconormal * 0.92
elif opcao == 3:
    total = preconormal
    parcela = total / 2
    print(f"a compra será parcelada em 2x de R$ {parcela:.2f} sem juros")
elif opcao == 4:
    total = preconormal * 1.25
    totalparcelas = int(input("Quantas parcelas? "))
    parcela = total / totalparcelas
    print(f"sua compra será parcelada em {totalparcelas}x de R$ {parcela:.2f} COM JUROS.")
else:
    total = preconormal
    print("opçao de pagamento inválida. tente denovo")

print(f"sua compra de R$ {preconormal:.2f} vai custar R$ {total:.2f} no final.")
