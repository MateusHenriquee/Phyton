nome= input("qual é o seu nome?")
print("prazer em conhece-lo{:20}!".format(nome))            #serve pra dar espaço
print("prazer em conhece-lo{:>20}!".format(nome))           #alinha o espaço pra direita
print("prazer em conhece-lo{:<20}!".format(nome))           #alinha o espaço pra esquerda
print("prazer em conhece-lo{:^20}!".format(nome))           #alinha no meio


slk= int(input("digite um valor:"))
pprt= int(input("digite outro valor:"))
soma= slk + pprt
print("a soma entre {}".format(soma))                           #criar variavel quando