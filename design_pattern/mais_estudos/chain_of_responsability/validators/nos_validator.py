from .interface import ValidatorInterface

class SquirrelHandler(ValidatorInterface):

    def validate(self, comida: str) -> bool:
        if comida == 'nos':
            return True
        return False

    def action(self) -> None:
        print('esquilo come nos')