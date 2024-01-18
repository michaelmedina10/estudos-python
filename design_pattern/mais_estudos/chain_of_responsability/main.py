from validators import MonkeyHandler, LionHandler, SquirrelHandler

class Validation:

    def __init__(self):
        self.val = [
            MonkeyHandler(),
            LionHandler(),
            SquirrelHandler(),
        ]

    def process(self, comida: str) -> str:
        for v in self.val:
            if v.validate(comida):
                return v.action()

validation = Validation()
validation.process('banana')
validation.process('nos')



"""
Problema classico para cadeia de responsabilidade, uma condicao, uma ou mais ações devem
ocorrer.
O código abaixo não é bom porque não é escalável, quanto mais condições mais ações.
"""

# class Validator:
#     def validar(self, comida: str):
#         if comida == 'banana':
#             self.__acao1()
#         elif comida == 'nos':
#             self.__acao2()
#         elif comida == 'carne':
#             self.__acao3()
#         else:
#             self.__acao_default()

#     def __acao1(self):
#         print("O macaco come banana")

#     def __acao2(self):
#         print("O esquilo come nos")

#     def __acao3(self):
#         print("O leao come carne")

#     def __acao_default(self):
#         print("comida indefinida")