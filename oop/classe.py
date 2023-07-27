class Carro:

    def __init__(self, nome) -> None:
        self.nome = nome

    # método de instãncia
    def acelerar(self):
        print("acelerando... vrum vrum")

c1 = Carro("fusca")
c1.acelerar()