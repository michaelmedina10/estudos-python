# GENERATOR FUNCTION

generator = (n for n in range(10000))

# Toda funcao com yield retorna um generator, caso eu coloque o return abaixo, ele será lançado como exceção quando não
# haver mais next()
def generator_func(n=0):
    yield 1 # Pausa
    print("continuando...")
    yield 2
    return "Lançado como execeção"

gen = generator_func(0)
print(gen)
print(next(gen))
print(next(gen))

# Se eu comentar a linha abaixo o generator estara vazio
gen = generator_func(1)
for n in gen:
    print("entrei")
    print(n)