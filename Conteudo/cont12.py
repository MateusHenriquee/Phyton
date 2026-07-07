# While infinito
# Nesse laço trabalhamos com um comando de parada que desvia a execução do bloco de código para o final do laço. Esse comando e chamado de break. Esse comando é executado em laços while que não possuem testes lógicos, onde escrevemos while true no loop, que sem o break seriam executados pra sempre.

# cont = 1

# while True:
#     print(cont, "->", end ="")
#     cont += 1
# print("Acabou")

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:    
        break
    s += n
print(f'A soma vale {s}')
