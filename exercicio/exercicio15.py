salario= float(input("salario atual: "))
clt= float(input("salário com aumento de:"))
promocao= salario + ( salario  * clt / 100)
print("o o salario de {:.2f} com aumento de {:.0f} porcento fica {:.2f} ".format(salario,clt,promocao))