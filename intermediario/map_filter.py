def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'produto5', 'preco': 1.50},
    {'nome': 'produto1', 'preco': 2.50},
    {'nome': 'produto2', 'preco': 3.50},
    {'nome': 'produto3', 'preco': 4.50},
]

def aumentar_valor(produto):
    return {
        **produto,
        'preco': produto['preco'] * 1.10
    }

# se não converter em uma lista o iterável, ao tentar usar mais de uma vez ele estará vazio
novos_produtos = map(aumentar_valor, produtos)
print('PRIMEIRO')
print_iter(novos_produtos)
print('SEGUNDO')
print_iter(novos_produtos)

print('FILTER')
produtos_filtrados = filter(lambda x: x['preco'] * 1.10, produtos)
print_iter(produtos_filtrados)