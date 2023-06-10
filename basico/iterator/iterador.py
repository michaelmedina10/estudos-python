palavra = "texto"
iterador = iter("texto")

# Como for funciona por baixo dos panos
while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break


for letra in palavra:
    print(letra)