from contextlib import contextmanager


@contextmanager
def my_open(caminho, modo):

    print("abrindo arquivo")
    arquivo =  open(caminho, modo, encoding='utf8')
    yield arquivo
    print("fechando arquivo")
    arquivo.close()

with my_open('arquivo_funcao.txt', 'w') as arquivo:
    arquivo.write("linha 1\n")
    arquivo.write("linha 2\n")
    arquivo.write("linha 3\n")
    print("DENTRO DO WITH", arquivo)