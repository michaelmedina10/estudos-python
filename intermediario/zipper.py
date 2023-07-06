from itertools import zip_longest

lista1 = ["SP", "BA", "MG", "RJ"]
lista2 = ['Ubatuba', 'Salvador', 'Belo Horizonte']

solucao1 = [tupla for tupla in zip(lista1, lista2)]
solucao2 = list(zip(lista1, lista2))
# usa a maior lista, iterável para construir as tuplas
solucao3 = list(zip_longest(lista1, lista2, fillvalue='SEM CIDADE'))
print(solucao1)
print(solucao2)
print(solucao3)