from random import sample

aluno1= input("NOME DO ALUNO1:")
aluno2= input("NOME DO ALUNO2:")
aluno3= input("NOME DO ALUNO3:")
aluno4= input("NOME DO ALUNO4:")
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = sample(lista, 4) 
print('a ordem de apresentação dos trabalhos dos alunos sera: {}'.format(escolhido))