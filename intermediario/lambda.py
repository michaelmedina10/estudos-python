lista = [
    {"nome": "Luiz"},
    {"nome": "Adriano"},
    {"nome": "MIhcael"},
]

# ordenar com função anônima, lambda
lista.sort(key=lambda obj: obj['nome'])
print(lista)