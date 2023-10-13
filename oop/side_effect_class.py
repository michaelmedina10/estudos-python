fichas  = [
    {
    "nome": "teste",
    "idade": 26,
    "endereco": {"rua": "rua teste", "numero": 123}
    },
    {
    "nome": "teste222",
    "idade": 2226,
    "endereco": {"rua": "rua test2222e", "numero": 123}
    }
]

class Instructions:

    def __init__(self) -> None:
        self.instructions: list = []
        self.fichas: list = []
        self._set_instructions()

    def get_instructions(self):
        return self.instructions

    def _set_instructions(self):
        self._get_fichas()
        self._include_ficha()
        self._include_dado_aleatorio()
        self._altera_todas_ruas()


    def _get_fichas(self):
        self.fichas = fichas.copy()

    def _include_ficha(self):

        for ficha in self.fichas:
            self.instructions.append(ficha)

    def _altera_todas_ruas(self):
        # Como pode ser visto alterando um objeto dentro da variavel instrucions
        # Alterando um valor dentro dessa lista de objetos em um laço, alterei realmente o endereco para endereco novo
        for _ficha in self.instructions:
            _ficha["endereco"]["rua"] = "endereco novo"

    def _include_dado_aleatorio(self):
        # Como pode ser visto alterando um objeto dentro da variavel instrucions
        # Alterando um valor dentro dessa lista de objetos em um laço, adicionei um novo campo em cada ficha no instructions e persiste
        # a ateração
        for _ficha in self.instructions:
            _ficha['valor_aleatorio'] = 10

instructions_obj = Instructions()
all_instructions = instructions_obj.get_instructions()
for instrucion in all_instructions:
    print(instrucion)

