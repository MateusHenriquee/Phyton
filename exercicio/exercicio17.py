carro= float(input("quantidade de km rodado com o carro: "))
alugado= float(input("dias alugado: "))
calculo= (alugado * 60 + carro * 0.15)
print("um carro alugado rodou {:.1f}km e cada km vale 0.15 centavos, cada dia alugado custa 60 reais, durante um periodo de {:.0f} dias, o total a pagar foi {:.2f} reais.".format(carro,alugado,calculo))