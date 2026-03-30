#import math
#nmr = int(input("digite um numero: "))
#nmrl= math.sqrt(nmr)
#print("a raiz de {} é igual a {}").format(nmr, math.ceil(nmrl))

#import math
#nmr = int(input("digite um numero: "))
#nmrl= math.sqrt(nmr)
#print("a raiz de {} é igual a {}").format(nmr, math.floor(nmrl))

#importando funcionalidades específicas

from math import sqrt,floor,ceil

nmr = int(input("digite seu numero: "))
nmrl = sqrt(nmr)
print("a raiz de {} é igual a {}".format(nmr, ceil(nmrl)))


import math
nmr = float(input("Digite um número"))
print("o valor digitado foi {} e a sua fração inteira é {}".format(nmr,math.trunc(nmr)))