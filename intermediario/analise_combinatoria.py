# Combination, Permutation and Product - Itertools
# Combinacao - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Product - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = ['Joao', 'Joana', 'Luiz', 'Letícia']
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['m', 'f']
    ]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

