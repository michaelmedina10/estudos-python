'''
 args  - Argumentos não nomeados
 * - *args (Empacotamento ouuu Desempacotamento)

 lembre-te de desempacotamento

 a, b, *resto = 1,2,3,4
 print(a, b, resto)
 out: 1, 2, [3,4]
'''

# Dessa forma EMPACOTA os argumentos passados pela função convertendo-os em uma tupla
def soma(*args):
    # return sum(args)
    return sum(args)

print(soma(1,2,3,45,66,7))

# Desempacotar, pega um iterável e espalha dentro da funcao
numeros = 1,2,3,4,5,6,7
print(soma(*numeros))

# printando o desempacotamento
print(type(*numeros))