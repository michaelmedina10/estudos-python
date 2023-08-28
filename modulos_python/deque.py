# Deque - Trabalhando com LIFO e FIFO

from collections import deque

lista = [0,1,2,3,4,5,6,7,8,9]

# LIFO - lista é tranquilo, append, adiciona ao final e pop, remove o último elemento
# FIFO - precisamos usar o deque pq pode vir a ser um processo custoso dado o volume de dados


# FIFO com deque
# Quando apendamos no lado esquerdo de uma lista, ele precisa reordenar todos os outros indices e isso pode ser muito custoso
# o deque tbm faz isso, masss, ele possui um algoritmo muito mais otimizado para realizar essa reordenação
fila_correta = deque()
fila_correta.append(3)
fila_correta.append(4)
fila_correta.append(5)
fila_correta.appendleft(0)
fila_correta.appendleft(1)
fila_correta.appendleft(2)
print(fila_correta)  # [2, 1, 0, 3, 4, 5]
fila_correta.pop()  # 5
fila_correta.popleft() # 2
print(fila_correta)  # deque([1, 0, 3, 4])
print(type(fila_correta))

