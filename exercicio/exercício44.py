
a = float(input("Digite o comprimento do lado A: "))
b = float(input("Digite o comprimento do lado B: "))
c = float(input("Digite o comprimento do lado C: "))

if a < b + c and b < a + c and c < a + b:
    print("Os lados formam um triângulo!")

    if a == b == c:
        print("Tipo: Equilátero (todos os lados iguais)")
    elif a == b or a == c or b == c:
        print("Tipo: Isósceles (dois lados iguais)")
    else:
        print("Tipo: Escaleno (todos os lados diferentes)")
else:
    print("Os valores informados não podem formar um triângulo.")
