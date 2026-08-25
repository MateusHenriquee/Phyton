# num = [2,5,9,1]
# num[2]= 3 #pode modificar a lista
# #num [4] = 7 #vai dar erro porque não tem esse indice na lista
# num.append(7)
# num.sort()
# num.sort(reverse=True)
# num.insert(2,0) #adiciona na posição 2 o valor de zero empurrando os outros elementos.
# num.insert(2,2) #adiciona na posição 2 o valor de zero empurrando os outros elementos.
# num.remove(2) # remove a primeira ocorrência
# num.remove(3) #da erro pois não exite o númro 4
# if 4 in num:
#     num.remove(4) #maneira certa de remover
# else:
#     print('não achei o número 4')
# num.pop(2) #elimina o elemento 2
# print(num)
# print (f'Essa lista tem {len(num)} elementos')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for c,v in enumerate(valores):
    print(f"na posição {c} eu achei o valor {v}. ", end="")
print(valores)
