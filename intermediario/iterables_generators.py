import sys


# sabe os valores que são apresentados
iterable = ['Eu', 'Tenho', '__iter__']
# Iterator só sabe chamar o proximo valor == __iter__() podendo usar o __next__()
iterator = iter(iterable)

generator = (n for n in range(10000))
lista = [n for n in range(10000)]

# Lista por exemplo salva todo valor em memória, o generator == iterator e não salva valores na memória ele te entrega o proximo caso use o next
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

# posso usar um laço for por exemplo no generator
# generator não esta na memoria, nao tem len, indice, nada

# Iterator é uma classe, que tem um iteravel e um iterator que chama next