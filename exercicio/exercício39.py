n1 = int(input("Digite um numero: "))
print('''Escolha uma das bases para a conversão:
[1] converter para binário
[2] converter para octal
[3] converter para hexadecimal''')# as 3 aspas permite escrever em mais de uma linha
opcao =int(input("Sua opção: "))
if opcao == 1:
    print("{} convertido para Binário é igual a {}".format(n1, bin(n1)))
elif opcao == 2:
    print("{} convertido para octal é igual a {}".format(n1,oct(n1)))
elif opcao == 3:
    print("{} convertido para hexadecimal é igual a {}".format(n1, hex(n1)))
else:
    print("Opção invalidada tente novamente")