# Abstract Base Class - Classe abstrata
# É possível usar @property com o @abstractmethod, @setter etc
# Classe abstrata não pode ser instanciada.
# Para ser abstrata, gerdade de ABC e precisa ter pelo menos um método abstrato

from abc import ABC, abstractmethod, ABCMeta


class log(ABC):

    @abstractmethod
    def _log(self, msg):
        pass

    # @abstractmethod
    # def _log(self, msg): ...


class LogPrintMixin(log):

    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

l = LogPrintMixin()
l._log('deu certo?')

print("#" * 100)

class AbstractFoo(metaclass=ABCMeta):

    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    # @property
    # @abstractmethod
    # def name(self): ...

    # @name.setter
    # @abstractmethod
    # def name(self, name): ...


class Foo(AbstractFoo):

    def __init__(self, name) -> None:
        super().__init__(name)

    # se a property esta na super classe, posso usá-la para gerar um setter
    @AbstractFoo.name.setter
    def name(self, name):
        self._name = name

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):
    #     self._name = name


f1 = Foo('Mic')
print(f1.name)
f1.name = 'Teste'
print(f1.name)
