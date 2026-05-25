# Laços de repetição for
# Em laços de repetição um bloco de código e executado diversas vezes. Para que o laço não se repita diversas vezes devemos impor limite. Nas linguagens de programação chamamos esse limite de variável de controle, que realiza uma comparação com um intervalo de tempo definido para parar de executar o bloco de códigos que está dentro do laço de repetição. Em python utilizamos a sintaxe: for + variável de controle + in + range(x,y):, sendo x o início do intervalo e y o fim do intervalo. As estruturas condicionais podem ser utilizadas dentro dos laços.

# Exemplo 1
# for c in range(0,6): #desconsidera o último
# print("oi")
# print("FIM")
# for c in range(0,6):
# print(c)
# print("FIM")
# for c in range(6,0,-1):# 0-1 faz ele contar em forma decrescente
# print(c)
# print("FIM")
# for c in range(0,6,2): # ele pula de 2 em 2
# print(c)
# print("FIM")

# Exemplo 2
# n = int(input("Digite um número: "))
# for c in range(0, n + 1 ): %+1 para chegar o número que eu quero
# print(c)
# print("FIM")
# i = int(input("Inicio: "))
# f = int(input("Fim: "))
# p = int(input("Passo: "))
# for c in range(i, f + 1 , p):%+1 para chegar o número que eu quero
# print(c)
# print("FIM")

s = 0
for c in range (0,4):
    n = int(input("Digite um valor: "))
    s += n #s = s + n
print(f"O somatório de todos os valores foi {s}")