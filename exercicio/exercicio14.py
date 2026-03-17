produto= float(input("preço do produto sem desconto: "))
valordesconto= float(input("valor desconto:"))
desconto= produto - ( produto * valordesconto / 100)
print("o produto que custa {:.2f} com desconto de {:.2f} porcento fica {:.2f} ".format(produto, valordesconto, desconto))