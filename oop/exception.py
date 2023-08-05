class MeuError(Exception):

    def __init__(self, msg: str) -> None:
        self.msg = msg

    def __str__(self) -> str:
        return self.msg

    # msg para o dev de como a classe foi montada
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        # !s aplica repr nos atributos retornando exatamente o que é o valor
        #!r retorna por exemplo a msg entre aspas, pois é string, se fosse um s ou sem nada ele colocaria o valor e poderia confundir
        # o dev sobre o tipo do valor
        return f'{class_name}({self.msg!r})'


def levantar():
    raise MeuError("VISH DEU ERRO!!!")


try:
    levantar()
except (MeuError, Exception) as e:  # except = se acontecer uma execeção com esse nome, faça tal coisa...
    print(e)


erro = MeuError('A')
print(repr(erro))