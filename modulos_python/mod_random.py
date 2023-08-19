import random

# random.randrange(inicio, fim, passo)
# -> Gera um número inteiro aleatório dentro de um intervalo especifico, com passo

r_range = random.randrange(10, 20, 2)  ## intervalo [10, 20] sempre de 2 em 2, ou seja, par
print(r_range)
# random.randint(inicio, fim)
# -> Gera um número inteiro aleatório dentro de um intervalo, sem passo

r_int = random.randint(10, 20)  ## intervalo [10, 20] sem o passo a passo
print(r_int)

# random.uniform(inicio, fim)
# -> Gera um número flutuante aleatório dentro de um intervalo, sem passo
r_uniform = random.uniform(10, 20) ## ponto flutuante
print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['a', 'b', 'c', 'd', 'e', 'f']
random.shuffle(nomes)
print(nomes)

# random.sample(SequenciaMutável, k = (tamanho da sample) Escolhe elementos do Iterável baseado em um tamanho de amostra
novos_nomes = random.sample(nomes, k=3)
print(novos_nomes)

# random.choices(Interável, k= (tamanho da sample)) -> Escolhe elementos do Iterável baseado em um tamanho de amostra
# mas esse pode repetir elementos na lista
novos_nomes = random.choices(nomes, k=3)
print(novos_nomes)

# random.choice(Interável) -> Escolhe um elemento do Iterável
novos_nomes = random.choice(nomes)
print(novos_nomes)