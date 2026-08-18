palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 
            'estudar', 'praticar', 'tecnologia', 'futuro', 'codigo',"slk",'oloko','nao','sim')

for palavra in palavras:
    print(f"\nNa palavra '{palavra.upper()}' temos as vogais: ", end="")

    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=" ")
