# Métodos de classe e factories
# Métodos de classe são métodos onde "self" será "cls", ou seja, ao invés de receber
# a instância no primeiro parametro iremos receber a próproa classe

class Pessoa:

    ano = 2023

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_classe(cls):
        print("SOU MÉTODO PERTENCENTE A CLASE, NÃO PRECISO DE UMA INSTÂNCIA PARA SER CHAMADA")

    # posso usar o classmethod para o padrão factory, um metodo que cria instancias, pois o cls é a propria classe, o molde
    # vamos criar uma classe para gerar pessoas com 50 anos

    @classmethod
    def gerar_pessoa_50_anos(cls, **infos):
        return cls(**infos)

    # metodo de instância
    def metodo_instancia(self):
        print("SOU MÉTODO PERTENCENTE A INSTANCIA, PRECISO DE UMA PARA SER INVOCADO!!!")


Pessoa.metodo_classe()
p1 = Pessoa.gerar_pessoa_50_anos(idade=26, nome="Michael")
p2 = Pessoa.gerar_pessoa_50_anos(nome="CLEUSANILDA", idade=1)

print(f"nome: {p1.nome}")
print(f"idade: {p1.idade}")
print("-" * 100)
print(f"nome: {p2.nome}")
print(f"idade: {p2.idade}")