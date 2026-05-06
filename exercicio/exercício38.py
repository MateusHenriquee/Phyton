salario = float(input("Salário do comprador: R$"))
casa= float(input("qual o valor da casa? R$"))
finaciamento = int(input("Quantos anos de financiamento?"))
prestacao = casa/(finaciamento*12)
if prestacao <= salario * 0.3:
    print("Para pagar uma casa de {} en {} anos a prestação será de R${:.2f} é suficiente. Emprestimo aprovado".format(casa, finaciamento, prestacao))
elif prestacao > salario*0.3:
    print("Para pagar uma casa de {} em {} anos a prestação será de R${:.2f} é muito pouco. Emprestimo negado".format(casa, finaciamento, prestacao))