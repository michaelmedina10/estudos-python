d1 = {
    "c1": 1,
    "c2": 2
}

# printa as keys em formato lista
print(list(d1))
print(tuple(d1))
print(list(d1.keys()))

# Printa os values em formato de lista
print(list(d1.values()))


# copy() == (shallow copy (cópia rasa))
# Copy, normalmente em dicionarios quando fazemos algo assim
# d1 = d2
# estamos passando o endereço de memória e não criando uma cópia do objeto, com o método copy(), conseguimos fazer isso
# desde que o dicionario tenha um nível de profundidade, para dict aninhados com outros dicionarios, obejtos, o copy mantem o endereço de memória

d2 = d1.copy()
d2['c1'] = 100
# D1 continua igual
print(d1)

# o método deepcopy faz uma cópia por completo do dicionario
from copy import deepcopy
d3 = {
    "c1": 100,
    "c2": [1,2,3,4,5]
}

d4 = deepcopy(d3)
d4["c2"][1] = 99999
print("print com deepcopy()")
print(d3, d4, sep="--")

# pop(chave) retorna o valor da chave especifica e apaga a chave passada, o popItem() retorna o valor da última chave e apaga