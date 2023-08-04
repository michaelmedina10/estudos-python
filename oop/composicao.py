# Relações  entre classes: associação, agregação e composição.
# Composiçãoe é uma especialização, da agregação.
# Mas nela quando o objeto Pai, for apagado, todas as referências dos objetos filhos são apagados tbm

# NO CASO ABAIXO COMO ESTAMOS GERANDO UMA INSTÂNCIA DO ENDERECO DENTRO DA CLASSE CLIENTE
# QUANDO O CLIENTE FOR APAGADO OS ENDERECOS SOMEM TBM
# SE EU TIVESSE PASSADO ENDERECO EXTERNO PARA DENTRO DA CLASSE SERIA AGREGAÇÃO E MESMO SEM O CLIENTE O ENDERECO
class Cliente:

    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print("############### APAGANDO #####")

class Endereco:

    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero

    # Garbidge Collector
    # O python verifica que uma variável não está sendo usada e deleta, com o metodo del
    def __del__(self):
        print("############### APAGANDO #####")

client1 = Cliente('MAria')
client1.inserir_endereco('Rua Lugar Nenhum', 22)
client1.listar_enderecos()
