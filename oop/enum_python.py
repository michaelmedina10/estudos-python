from enum import Enum

# direcoes = enum.Enum('direcoes', ['ESQUERDA', 'DIREITA'])

class Direcoes(Enum):
    ESQUERDA = 1
    DIREITA = 2


def mover(direcao):
    print(f"Movendo para {direcao.value}")

mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)