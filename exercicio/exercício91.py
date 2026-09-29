ficha = []
while True: 
    nome = str(input("nome:" ))
    nota1 = float(input("nota 1: "))
    nota2 = float(input("nota 2: "))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2], media])
    resp = str (input("quer continuar? "))
    if resp in "Nm":
        break
print(f"{"n":<4} {"nome":<10} {"media":<8}")

for i,a in enumerate(ficha):
    print(f"{i:<4} {a:[0]:<10} {a[2]:>8}")
    
while True:
    opc = int(input("mostrar notas de qual aluno?(999 interrompe)"))
    if opc == 999:
        break
    if opc <=len(ficha)-1:
        print(f"notas de {ficha[opc] [0]} sÕ {ficha [opc] [1]}")
