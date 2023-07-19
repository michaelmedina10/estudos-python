from functools import reduce

produtos = [
    {'nome': 'produto5', 'preco': 1.50},
    {'nome': 'produto1', 'preco': 2.50},
    {'nome': 'produto2', 'preco': 3.50},
    {'nome': 'produto3', 'preco': 4.50},
]

# total = acumulador
def funcao_do_reduce(total, produto):
    total += produto['preco']
    return total

# 0 valor inicial
total = reduce(funcao_do_reduce, produtos, 0)

print(total)