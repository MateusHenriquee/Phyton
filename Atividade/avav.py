def verifica_colchetes(expressao):
    pilha = []
    
    for caractere in expressao:
        if caractere == '[':
            pilha.append(caractere)
        elif caractere == ']':
            if not pilha:
                return False
            pilha.pop()
            
    return len(pilha) == 0

entrada = input("Digite a expressão com colchetes: ")

if verifica_colchetes(entrada):
    print("expressão correta")
else:
    print("expressão incorreta")
