frase = '     Olha só que,     coisa interessante'
lista_frases_cruas = frase.split(',')

lista_frases = []

for i, _ in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

# join tu primeiro passa qual sera o criterio de espaçamento para o iterador

print('-'.join('abc'))
## out: a-b-c = string é um iteravel

# lista tbm é iteravel
print(''.join(lista_frases))
