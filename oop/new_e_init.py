from typing import Self


class A:

    # new é executada quando instanciamos um objeto
    # depois do __new__ é camado o __init__ "construtor" de nossa classe
    def __new__(cls, *args, **kwargs) -> Self:
        print("Antes da instancia")
        instancia = super().__new__(cls)
        print("gerei a inst, vou retornar")
        return instancia

    def __init__(self) -> None:
        print("SOU O INIT")

a = A()