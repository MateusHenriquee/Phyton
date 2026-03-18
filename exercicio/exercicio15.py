salario= float(input("salario atual: "))
clt= float(input("salário com aumento de:"))
promocao= salario + ( salario  * clt / 100)
print("o o salario de {:.2f} reais com aumento de {:.0f}% porcento fica {:.2f} reais ".format(salario,clt,promocao))