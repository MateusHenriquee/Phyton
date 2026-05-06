# Condições aninhadas
# São condições colocadas dentro de outras condições. Em condições aninhadas eu utilizo o se não se, dentro do se. Em python o se não se é representado por elif condição. A partir do primeiro elif para mais condições você vai colocando um elif para cada condição. Sempre que for usar o primiero elif tem que usar um if antes e o else se torna opcional.

nome = str(input("qual é o seu nome? "))
if nome == "slk":
    print("que nome bonito")
elif nome == "am" or nome == "an" or nome == "ata":
    print("q nome diferenciado, seu bst")
elif nome in " bla sla oloko massa":
    print("interessante")
else:
    print("seu nome é normal")
