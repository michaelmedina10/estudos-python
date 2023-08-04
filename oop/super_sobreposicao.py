# super() é a super classe na sub classe

# Classe principal Pessoa
# -> super class, base class, parent class

# Classes filhas (Cliente)
# -> sub class, child class, derived class


# ORDEM DE BUSCA EM CLASSES
# CLASSE CHAMADA
# SUPER CLASSE OU PAI
# BUILTINS OBJECT

# MINHACLASSE
# STR
# BUILTINS OBJECT

class MinhaString(str):

    def upper(self):

        print('MEU UPPER')
        retorno = super().upper()
        print('EXECUTEI UPPER DA CLASSE STRING')
        return retorno

p1 = MinhaString('Michael')
print(p1.upper())


print("#" * 100)
class A:

    def metodo(self):
        print('A')

class B(A):

    def metodo(self):
        print('B')

class C(B):

    def metodo(self):
        super().metodo() #B
        super(B, self).metodo() #A
        # super(A, self).metodo() # NAO FUNCIONA PQ CLASSE OBJECT NAO TEM METODO, CHEGUEI NO TOPO DA HIERARQUIA
        print('C')

c = C()
c.metodo()