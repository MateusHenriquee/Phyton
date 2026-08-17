# # Tuplas(variáveis compostas)

# # Relembrando do primeiro trimestre, toda vez que um variável simples é declarada um espaço na memória e criado no computador. Onde valores são guardados pelo operador de . Em variáveis simples se eu quiser guardar mais um valor dentro do espaço criado na memória o que estava armazenado anteriormente é excluido e o novo valor é armazenado. Para resolvermos esse problema podemos criar mais espaços na memória em uma mesma variável, e uma dessas formas e com o uso de tuplas. Os elementos de uma tupla pode ser selecionados através de seus índices que inicia-se no valor 0

# # Tuplas(variáveis compostas)
# # Dentro das tuplas podemos usar métodos de fatiamento, de length e o uso das variáveis de repetição. As tuplas são imutáveis em Python ou seja os valores armazenados nessas variáveis não podem ser alterados após definidos. As tuplas são definidas entre parënteses

# # sla = ("amburgue","agua","pao","sim") exemplo 1
# # print(sla)
# # print(sla[1])
# # print(sla[-2])
# # print(sla[1:3])
# # print(sla[2:]) 
# # print(sla[:2])
# # print(sla[-2:])

# # lanche= ('Hamburguer', 'Suco', 'Pizza', 'Pudim') exemplo 2
# # for comida in lanche:
# #     print(f'Eu vou comer (comida)')
# # print('comi pra caramba')
# # print(len(lanche))
# # for cont in range(0, len(lanche)):
# #     print(f'Eu vou comer (lanche [cont]) na posição (cont)') #outra forma de fazer

# exemplo 3

# lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# print(sorted(lanche))#ordena em ordem alfabética
# a = (2, 5, 4)
# b = (5,8,1,2)
# print(a)
# print(b)
# c = a + b
# print(c)
# print(len(c))
# print(c.count(5))#quantas vezes esta aparecendo o 5 em c
# print(c.index(8))#mostra a posição pegando a primeira ocorrencia
# print(c.index(5, 2))# começa a partir da posição 2
