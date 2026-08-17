print("Gerador de Sequência")
print("-=" * 10)

termo1 = 0
termo2 = 1
cont = 3
total = 0
mais = 10 # Começa mostrando os 10 primeiros termos

while mais != 0:
    total = total + mais
    while cont <= total:
        # Exemplo com Fibonacci, mas a lógica de repetição serve para qualquer sequência
        termo3 = termo1 + termo2
        print(f"{termo3} -> ", end="")
        termo1 = termo2
        termo2 = termo3
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print(f"Progressão finalizada com {total} termos mostrados.")
