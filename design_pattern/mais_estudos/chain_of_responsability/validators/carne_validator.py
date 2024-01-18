from .interface import ValidatorInterface

class LionHandler(ValidatorInterface):

    def validate(self, comida: str) -> bool:
        if comida == 'carne':
            return True
        return False

    def action(self) -> None:
        print('leão come carne')