import random

vitorias = 0

print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 15)

while True:

    jogador_valor = int(input("Diga um valor: "))
    
    jogador_escolha = " "
    while jogador_escolha not in "PI":
        jogador_escolha = input("Par ou Ímpar? [P/I] ").strip().upper()[0]
    
    computador_valor = random.randint(0, 10)
    total = jogador_valor + computador_valor
    resultado = "P" if total % 2 == 0 else "I"
  
    print("-" * 30)
    print(f"Você jogou {jogador_valor} e o computador {computador_valor}.")
    print(f"Total de {total} -> DEU " + ("PAR" if resultado == "P" else "ÍMPAR"))
    print("-" * 30)

    if jogador_escolha == resultado:
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        print("=-" * 15)
        vitorias += 1
    else:
        print("Você PERDEU!")
        print("=-" * 15)
        break

print(f"GAME OVER! Você venceu {vitorias} vezes consecutivas.")
