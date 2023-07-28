# Métodos staticos são funcões dentro de sua classe, ela não tem acesso ao self e nem ao cls, talvez alguem a use por
# organização, masss, não tem muito sentido em usar esse

class Classe:

    @staticmethod
    def metodo_estatico():
        print("SOU ESTATICO POSSO SER CHAMADO POR INSTANCIA OU DIRETO PELA CLASSE")

c1 = Classe
c1.metodo_estatico()
Classe.metodo_estatico()