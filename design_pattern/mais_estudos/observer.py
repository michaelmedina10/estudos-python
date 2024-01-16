from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange


# Observer of the pattern
class Subject(ABC):

    @abstractmethod
    # cadastra Observer
    def attach(self, observer: Observer) -> None : pass

    @abstractmethod
    # remove observer
    def detach(self, observer: Observer) -> None: pass

    @abstractmethod
    # notifica observers
    def notify(self, observer: Observer) -> None: pass


class ConcreteSubject(Subject):

    # Estado que ao ser alterado ira notificar os subinscritos
    _state = None

    # lista de inscritos
    _observers: list[Observer] = []


    # função para cadastrar observer
    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    # função para remover observer
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)


    # Função para notifica observers
    def notify(self) -> None:

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update()

    def some_business_logic(self) -> None:
        """
        Aqui vai as lógicas que irão alterar algum estado e com isso iremos avisar a todos os
        observers que algo mudou e eles decidem o que faz
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()

# Other Subject
class OtherSubject(Subject):

    # Estado que ao ser alterado ira notificar os subinscritos
    _state = None

    # lista de inscritos
    _observers: list[Observer] = []


    # função para cadastrar observer
    def attach(self, observer: Observer) -> None:
        print("Other Subject: Attached an observer.")
        self._observers.append(observer)

    # função para remover observer
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)


    # Função para notifica observers
    def notify(self) -> None:

        print("Other Subject: Notifying observers...")
        for observer in self._observers:
            observer.update()

    def some_business_logic(self) -> None:
        """
        Aqui vai as lógicas que irão alterar algum estado e com isso iremos avisar a todos os
        observers que algo mudou e eles decidem o que faz
        """

        print("\Other Subject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Other Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""

# recebendo o observable eu posso escolher quem minhas class irão observar
class ConcreteObserverA(Observer):

    def __init__(self, subject: Subject) -> None:
        self.subject = subject


    def update(self) -> None:
        if self.subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):

    def __init__(self, subject: Subject) -> None:
        self.subject = subject


    def update(self) -> None:
        if self.subject._state == 0 or self.subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()
    other_subject = OtherSubject()

    observer_a = ConcreteObserverA(subject)
    subject.attach(observer_a)

    observer_b = ConcreteObserverB(other_subject)
    other_subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()