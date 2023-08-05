from abc import ABC, abstractmethod

# ideal seria fazer com classe abstrata, mas a aula é sobre polimorfismo, exemplo abaixo
# class Mamifero(ABC):

#     @abstractmethod
#     def emitir_som(self): ...

#     @abstractmethod
#     def mover(self): ...


class Mamifero(ABC):

    def emitir_som(self):
        print("emitindo algum som!!!")

    def mover(self):
        print("me movendo")


class Cachorro(Mamifero):

    def emitir_som(self):
        print("AU AU AU!!!")

    def mover(self):
        print("ANDANDO")


class Macaco(Mamifero):

    def emitir_som(self):
        print("AAA UUU AAAA!!!")

    def mover(self):
        print("ANDANDO E PULANDO")


c = Cachorro()
c.emitir_som()
c.mover()

print("*" * 100)
c = Macaco()
c.emitir_som()
c.mover()