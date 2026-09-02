expressao = str(input("Digite uma expressão matemática: "))

pilha = []
correta = True

for caractere in expressao:
    if caractere == '(':
        pilha.append('(') 
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()    
        else:
            correta = False 
            break

if correta and len(pilha) == 0:
    print("Sua expressão está com os parênteses na ordem correta!")
else:
    print("Sua expressão está errada! Parênteses mal posicionados.")
