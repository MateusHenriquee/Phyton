nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
print("Sua média foi: {:.1f}".format(media))

if media < 5.0:
    print("Status: Reprovado")
elif 5.0 >= media <= 6.0:
    print("Status: Recuperação")
else:
    print("Status: Aprovado")
