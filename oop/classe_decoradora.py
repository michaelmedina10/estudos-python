from typing import Any


class Multiplicar:

    def __init__(self, multiplicar) -> None:
        self.multiplicar = multiplicar

    def __call__(self, func) -> int:

        # lembre-se sempre que preciso adiar a execução de uma função, uso closure
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicar
        return interna

@Multiplicar(10)
def somar(x: int, y: int):
    return x + y

resultado = somar(2, 4)
print(resultado)