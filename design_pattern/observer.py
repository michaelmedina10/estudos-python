"""
Padrão observer tem a intenção de definir uma dependencia de um-para-muitos entre
objetos , de maneira que quando um objeto muda o estado, todos os seus dependentes
são notificados e atualizados automaticamente.

observer é um objeto que gostaria de ser informado, um observable (subject) é a entidade
que gera as informações.
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class IObservable(ABC):

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass


# Quem quero observar
class WeatherStation(IObservable):

    # Observable
    def __init__(self) -> None:
        self._observers: list[IObserver] = []
        self._state: dict = {}

    @property
    def state(self) -> dict:
        return self._state

    @state.setter
    def state(self, state_update: dict) -> None:
        new_state = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()

# ----------------------------------------------------------------
class IObserver(ABC):
    #Observer
    @abstractmethod
    def update(self) -> None: pass


class SmartPhone(IObserver):
    # Observer
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} acabou de ser atualizado => {self.observable.state}')

class Notebook(IObserver):

    # Observer
    def __init__(self, observable: IObservable) -> None:
        self.observable = observable

    def show(self) -> None:
        state = self.observable.state
        print('Sou outro Observador, posso fazer outra coisa', state)

    def update(self) -> None:
        self.show()


if __name__ == '__main__':

    weather_station = WeatherStation()

    smartphone = SmartPhone('Iphone', weather_station)
    outro_smartphone = SmartPhone('outro_smartphone', weather_station)
    notebook = Notebook(weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(outro_smartphone)
    weather_station.add_observer(notebook)

    weather_station.state = {"temperature": "20C"}
    print()
    weather_station.state = {"temperature": "32C"}
    print()

    weather_station.remove_observer(outro_smartphone)
    weather_station.reset_state()