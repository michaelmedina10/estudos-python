from typing import Self

# Ao gerar uma classe algumas coisas ocorrem por padrão
# __new__ da metaclasse é chamado para gerar a classe
# __call__ da metaclasse é chamado com os argumentos e depois chama o:
#   __new__ da classe que gera a instância
#   __init__ da classe que inicializa a instancia com os argumentos
# __call__ da metaclasse finaliza a execução

class Meta(type):

    def __new__(mcs, name, bases, dct):
        print("Criando a classe")
        cls = super().__new__(mcs, name, bases, dct)
        return cls

    def __call__(self, *args, **kwargs):
        print("__call__ da metaclasse")
        instancia = super().__call__(*args, **kwargs)
        if 'nome' not in instancia.__dict__:
            raise NotImplementedError("crie o attr nome")
        return instancia


# Até aqui tudo bem, ja tenho a classe e crio instancia e inicializo
class Pessoa(metaclass=Meta):

    def __new__(cls, *args, **kwargs) -> Self:
        print("Gerando instancia")
        instancia = super().__new__(cls)
        print("instancia gerada")
        return instancia

    def __init__(self, nome) -> None:
        print("Recebi a instancia, SOU INIT")
        # self.nome = nome

p1 = Pessoa('Michael')