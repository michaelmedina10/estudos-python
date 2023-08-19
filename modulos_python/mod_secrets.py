# Secrets gera números aleatórios fortemente criptografados baseados na aleatoriedade mais forte que seu S.O fornece

import secrets

print(secrets.randbelow(100))
print(secrets.choice([1,2,4,5]))


# Jogar o secret no range para trabalhar
random = secrets.SystemRandom()  # foi dica do curso isso, mas os metodos invocados abaixo pertencem a classe SystemRandom

# Agr posso usar o random sendo realmente aleatorio o seed não interfere mais mesmo se for inicializado

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
