# @property - um getter no modo Pythonico
# getter - um método para obter um atributo
# modo pythônico - modo do Python de fazer coisas
# @property - é uma propriedade do objeto, ela é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
#   - como getter
#   - p / evitar quebrar código cliente
#   - p / abilitar setter
#   - p/ executar ações ao obter um atributo


class Caneta:
    def __init__(self, cor) -> None:
        self._cor = cor

    @property
    def cor(self):
        return self._cor

    # Para usar o decorator cor, ele precisa ser uma property
    @cor.setter
    def cor(self, cor):
        self._cor = cor

c1 = Caneta('AZULL')
print(c1.cor)
c1.cor = 'VERMELHO'
print(c1.cor)

# Por convenção usamos um ou dois underlines para indicar para devs que não queremos que essa variável seja usada no código, mas
# ainda posso alterá-la
c1._cor = 'Amarelo'
print(c1.cor)