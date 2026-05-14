from datetime import date
ano =int(input("Ano de nascimento "))
idade = date.today().year - ano
tempopassado = idade - 18
tempofaltante = 18 - idade
print("Quem nasceu em {} tem {} anos".format(ano,idade))
if idade> 18:
    print("Você já deveria ter se alistado há {} anos".format(tempopassado))
elif idade < 18:
    print("Você ainda não tem idade para se alistar faltam {} anos".format(tempofaltante))
else:
    print("Você deve se alistar esse ano")