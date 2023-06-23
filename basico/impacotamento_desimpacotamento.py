"""
    Introdução ao impacotamento e ao desimpacotamento + tuples()
"""

nomes = ["cleusanilda", "jubileu", "juvenal"]
nome1, nome2, nome3 = nomes
print(nome1)

print("-" * 10 )

# Pegando só uma variável e armazenando o resto em outra variável
nome1, *resto = nomes
print(nome1)
print(resto)