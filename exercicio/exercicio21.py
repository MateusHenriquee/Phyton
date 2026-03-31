from random import choice

aluno1= input("NOME DO ALUNO1:")
aluno2= input("NOME DO ALUNO2:")
aluno3= input("NOME DO ALUNO3:")
aluno4= input("NOME DO ALUNO4:")
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice (lista) #escolhe um da lista
print('o aluno escolhido foi {}'.format(escolhido))