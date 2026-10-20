from datetime import datetime

dados = {}
dados['nome'] = str(input("digite o seu nome: "))
nasc = int(input("em qual ano você nasceu? "))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input("qual é o seu ctps? "))
if dados ['ctps'] != 0:
    dados["contratacao"] = int(input("ano de contratacao: "))
    dados["salário"] = float(input("salário: "))
    dados["aposentadoria"] = ((dados["contratacao"] +35 ) - datetime.now().year)
for k,v in dados.items():
    print(f"{k} tem o valor {v}")