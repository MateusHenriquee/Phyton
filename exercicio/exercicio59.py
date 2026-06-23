# Inicializa a variável com um valor vazio
sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]

# Enquanto o valor não for 'M' nem 'F', o programa pede novamente
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]

print(f'Sexo {sexo} registrado com sucesso.')
