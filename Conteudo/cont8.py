# Condições
# Estrutura sequencial: Os comandos condicionais são executados de cima para baixo em um bloco de códigos. Até esse momento estávamos trabalhando nessa lógica, porém nas estruturas condicionais temos duas possibilidades de caminhos. Cada caminho terá um bloco de comando executados se ele for escolhido. Em programação utilizamos o comando se, se alguma condição verdadeira executa um bloco de códigos, e podemos utilizar um bloco se não para executar quando a condição for falsa.

# Em condicionais devemos deixar o código indentado, ou seja, com o espaçamento correto demonstrando qual bloco de código pertece ao operador condicional. Para realizar a indentração podemos utilizar a tecla tab. Em python para o se utilizamos if+confição+:, já o senão utilizamos o else +:, depois dos dois pontos nos dois casos colocamos os blocos de códigos que serão executados. Nesse tipo de condicional apenas um bloco é executado.

# tempo = int(input("Quantos anos tem seu carro?"))

# if tempo<=3:
    # print('carro novo')
# else:
    # print('carro velho')
# print('--fim--')

# Condições simplicaficada (exemplo)
# tempo= int(input("Quantos anos tem seu carro?"))
# print('carro novo' if tempo<=3 else'carro velho')
# print('--fim--')

# nome = str(input('Qual é o seu nome? '))
# if nome == 'mano':
#     print('Que nome lindo você tem!')
# else:
#     print('seu nome é tão normal')
# print('Bom dia {}!'.format(nome))

# Condições simplicaficada (exemplo)

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
m = (n1 + n2)/2
print("A sua média foi {:.1f}".format(m))
if m >= 6.0:
    print("A sua média foi boa Parabéns ae")
else:
    print("Sua média foi ruim! seu lixoso, estude mais")
print("Parabéns seu merda" if m >= 6 else "Estude mais, seu inutil")