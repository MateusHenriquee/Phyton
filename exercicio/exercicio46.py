print("=" * 11 + " LOJAS SANTOS " + "=" * 11)

# Entrada do preço das compras
preco = float(input("Preço das compras: R$ "))

# Exibição das formas de pagamento
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')

# Entrada da opção de pagamento
pagamento = int(input("Qual é a opção? "))

# Condições para cada forma de pagamento
if pagamento == 1:
    desconto = preco - (preco * 0.1)
    print("Sua compra com o desconto à vista fica R${:.2f}".format(desconto))
elif pagamento == 2:
    desconto = preco - (preco * 0.05)
    print("Sua compra à vista no cartão fica R${:.2f}".format(desconto))
elif pagamento == 3:
    cartao = preco / 2
    print("Sua compra parcelada no cartão fica 2x de R${:.2f}".format(cartao))
elif pagamento == 4:
    parcela = int(input("Digite o número de parcelas: "))
    juros = preco + (preco * 0.2)
    total = juros / parcela
    print("A sua compra no cartão vai ser feita em {} parcelas e o valor com juros de cada parcela fica R${:.2f}".format(parcela, total))
else:
    print("Opção inválida de pagamento. Tente novamente.")