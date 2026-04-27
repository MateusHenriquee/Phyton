# Condições
# Estrutura sequencial: Os comandos condicionais são executados de cima para baixo em um bloco de códigos. Até esse momento estávamos trabalhando nessa lógica, porém nas estruturas condicionais temos duas possibilidades de caminhos. Cada caminho terá um bloco de comando executados se ele for escolhido. Em programação utilizamos o comando se, se alguma condição verdadeira executa um bloco de códigos, e podemos utilizar um bloco se não para executar quando a condição for falsa.

# Em condicionais devemos deixar o código indentado, ou seja, com o espaçamento correto demonstrando qual bloco de código pertece ao operador condicional. Para realizar a indentração podemos utilizar a tecla tab. Em python para o se utilizamos if+confição+:, já o senão utilizamos o else +:, depois dos dois pontos nos dois casos colocamos os blocos de códigos que serão executados. Nesse tipo de condicional apenas um bloco é executado.

tempo = int(input("Quantos anos tem seu carro?"))

if tempo<=3:
    print('carro novo')
else:
    print('carro velho')
print('--fim--')