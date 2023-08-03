
# Publico - visivel para todo projeto
# Protected - visivel para classe e subclasses
# Private - visivel somente na classe que foi criada
class Foo:

    def __init__(self):
        self.publico = 'PUBLICO'
        self._protected = 'PORTECTED'
        self.__private = 'PRIVATE'

    def acessar_privado(self):
        print(self.__private)
        print('printei o privado dentro da classe, fora ele modifica o nome para _Foo__private, para vc não usar mesmo')

f1 = Foo()
print(f1.publico)
print(f1._protected)
print(f1._Foo__private)
f1.acessar_privado()