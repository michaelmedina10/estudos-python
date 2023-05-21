lista = [1, 2, 3, 4, 5, 6, 7, 9, 10]

def imprimir_lista(*lista):
    print(type(lista))
    [print(item) for item in lista]

imprimir_lista(*lista)