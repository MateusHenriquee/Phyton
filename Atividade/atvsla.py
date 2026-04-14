nome_completo = input("Digite seu nome completo: ").strip()

partes_nome = nome_completo.split()

segundo_nome = partes_nome[1]

print("O segundo nome tem {} letras.".format({len(segundo_nome)}))