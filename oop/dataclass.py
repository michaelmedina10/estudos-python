from dataclasses import dataclass, field


# dataclass ja cria para nós o init, repr e eq
@dataclass(init=True)
class Pessoa:

    _nome: str
    _idade: float
    enderecos: list[str] = field(default_factory=list)

    def __post_init__(self):
        print("depois do init")

    @property
    def nome(self):
        return self._nome


if __name__ == "__main__":
    p1 = Pessoa('micael', 26)
    print(p1)