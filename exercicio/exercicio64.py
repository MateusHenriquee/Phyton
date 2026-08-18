print("Gerador de Sequência")
print("-=" * 10)

termo1 = 0
termo2 = 1
cont = 3
total = 0
mais = 10 

while mais != 0:
    total = total + mais
    while cont <= total:

        termo3 = termo1 + termo2
        print(f"{termo3} -> ", end="")
        termo1 = termo2
        termo2 = termo3
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))

print(f"Progressão finalizada com {total} termos mostrados.")
