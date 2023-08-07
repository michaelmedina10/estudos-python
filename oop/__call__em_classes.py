# Método callable ou __call__
# callable é algo que podemos executar usando os parenteses
# Em classes o método call faz a instância de uma classe

class CallMe:

    def __init__(self, phone) -> None:
        self.phone = phone

    # Permite a instância ser chamada como um executável
    def __call__(self, nome):
        print(nome, "Está te chamando!!!")
        return 'posso retornar ou fazer o que quiser'

call1 = CallMe('1233455')
retorno = call1('Michael')
print(retorno)