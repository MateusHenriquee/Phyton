# Listas parte 2
# Podemos adicionar uma lista dentro de outra lista. Para isso utilizamos a sintaxe nome da lista. append(nome da outra lista [:]), cada lista adicionada vira um elemento dentro da lista externa. Podemos declarar de forma direta igualando a lista externa as listas que eu quero adicionar colocando os dados entre colchetes e separando cada conjunto de lista por virgula. Ex pessoas = [['pedro', 75], ['maria', 19],['joao',32]]. O indices de cada lista são 0, 1, 2 respectivamente.

# Para mostrar-mos um item dentro de uma lista interna primeiro colocamos o índice da lista depois o índice do item dentro da lista. Ex print(pessoas[0][0]) irá mostrar 'pedro', print (pessoas[1][1] vai aparecer 19, print(pessoas[2][0]) vai aparecer joão, print(pessoas[1]) vai aparecer ['maria',19]

# exemplo 1

# teste = []
# teste.append("sla")
# teste.append(1)
# galera = []
# galera.append(teste)
# galera.append(teste[:])
# teste [0] = "m"
# teste [1] = 0
# galera.append(teste[:])
# print(teste)
# print(galera)

# exemplo 2

# galera = [['sla', 19], ["nsei", 1],["nao", 0],["sim" ,10]]

# print(galera[2][1])

# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

galera = []

dado = []

que = q = 0

for c in range (0,3):
    dado.append(str(input("nome: ")))
    dado.append(int(input("idade: ")))
    galera.append(dado)
    dado.clear()
print(galera)
    