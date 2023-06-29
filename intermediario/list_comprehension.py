produtos = [
    {"produto": "celular1", "preco": 2000},
    {"produto": "celular2", "preco": 3000},
    {"produto": "celular3", "preco": 4000},
]

# IF a esquerda do for precisa do else == mapeamento
# IF a direita é filtro, nao tem else == filtro
lista1 = [
    {**produto, "preco": produto["preco"] * 0.80}
    if produto["preco"] == 2000 else {**produto}
    for produto in produtos
]
print(lista1)