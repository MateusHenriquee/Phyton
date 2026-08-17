numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

digitado = int(input('Digite um número entre 0 e 20: '))

while True:
    if digitado < 0 or digitado > 20:
        digitado = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break

print(f'Você digitou o número {numeros[digitado]}')
