# Funções decoradoras e decoradores
# Decorar = Adicionar | Remover | Restringir | Alterar
# Funções decoradoras são funções ue decoram outras funções
# Decoradores são usados para fazer o python usar as funções decoradores em outras funções
# Decoradores são sintaxe_sugar (Áçucar sintático) ou seja a linguagem tem recursos que facilitam o uso das funções decoradoras


def criar_funcao(func):

    def interna(*args, **kwargs):
        print("vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f"O seu resultado foi {resultado}")
        print("Foi decorada!!!")
        return resultado
    return interna


def e_string(arg):
    if not isinstance(arg, str):
        raise TypeError("Argumento deve ser uma string, oxee!!!")

# Para aplicar a função criar_funcao podemos usar o decorator, funções iniciadas com @
@criar_funcao
def inverte_string(string):
    return string[::-1]

# usando a função decoradoras sem a sintaxe do decorator
# inverte_string_checando_parametro = criar_funcao(inverte_string)
# string_invertida = inverte_string_checando_parametro(123)
# print(string_invertida)
string_invertida = inverte_string("123")
print(string_invertida)