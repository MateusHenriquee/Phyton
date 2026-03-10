nome= input("nome do aluno:")
nota1= float(input("valor da sua primeira nota:"))                  #float pq o numero da nota pode ser numero com virgula tlgd
nota2= float(input("valor da sua segunda nota:"))
soma= nota1 + nota2

print("nome do aluno: {} sua primeira nota foi {} e sua segunda nota foi {} e a sua média é: {}" .format(nome, nota1, nota2, (soma)/2))
