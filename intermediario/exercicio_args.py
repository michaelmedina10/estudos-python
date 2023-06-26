from numpy import prod

def multiplicar(*numeros) -> int:
    return prod(numeros)

total_multiplicado = multiplicar(1,2,3)
print(total_multiplicado)


def verificarParOuImpar(num: str) -> str:
    return 'PAR' if num % 2 == 0 else 'ÍMPAR'

parOuImpar = verificarParOuImpar(3)
print(parOuImpar)