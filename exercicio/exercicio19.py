from math import hypot
cateto1= float(input("digite o cateto adjacente: "))
cateto2= float(input("digite o cateto oposto: "))
hipotenusa= hypot(cateto1,cateto2)
print("tendo cateto adjacente como {} e o cateto oposto como {} o valor da hipotenusa é: {}".format(cateto1,cateto2, hipotenusa))