mais_de_18 = 0
total_homens = 0
mulheres_menos_20 = 0

while True:
    print("-" * 20)
    print("CADASTRE UMA PESSOA")
    print("-" * 20)

    idade = int(input("Idade: "))

    sexo = " "
    while sexo not in "MF":
        sexo = input("Sexo: [M/F] ").strip().upper()

    if idade > 18:
        mais_de_18 += 1
        
    if sexo == "M":
        total_homens += 1
        
    if sexo == "F" and idade < 20:
        mulheres_menos_20 += 1

    resposta = " "
    while resposta not in "SN":
        resposta = input("Quer continuar? [S/N] ").strip().upper()

    if resposta == "N":
        break

print("\n" + "=" * 30)
print(" FIM DO PROGRAMA ")
print("=" * 30)
print(f"a) Total de pessoas com mais de 18 anos: {mais_de_18}")
print(f"b) Ao todo temos {total_homens} homens cadastrados.")
print(f"c) E temos {mulheres_menos_20} mulheres com menos de 20 anos.")
