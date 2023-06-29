produto = {
    'nome': 'teste',
    'preco': 1.05,
    'categoria': 'escritório'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in produto.items()
}
print(dc)

# set
s1 = {i for i in range(10)}
print(s1)

# assim é melhor, foi só um exemplo acima
s2 = set(range(10))
print(s2)