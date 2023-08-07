# Duck typing com __enter__ e __exit__

# Vamos ensinar nossa classe a trabalhar com contexto abaixo, "dar a habilidade dela abrir contextos"
# with open('caminho.txt', 'w') as file:
#     ...


# class MyContextManager:

#     def __enter__(self):
#         print("ENTER")

#     def __exit__(self, exc_class, exc_value, traceback_):
#         print("EXIT")


# instancia = MyContextManager()

# with instancia as alguma_coisa:
#     print("DENTRO DO WITH")

# # output: ENTER, DENTRO DO WITH, EXIT
# # variavel alguma_coisa é None, pq o enter não retornou nada!!!

class MyContextManager:

    def __init__(self, caminho, modo) -> None:
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None


    def __enter__(self):
        print("ABRINDO")
        self._arquivo = open(self.caminho, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, exc_class, exc_value, traceback_):
        print("SAINDO")
        return self._arquivo.close()


instancia = MyContextManager()

with instancia as arquivo:
    arquivo.write("linha 1")
    arquivo.write("linha 2")
    arquivo.write("linha 3")
    print("DENTRO DO WITH", arquivo)
