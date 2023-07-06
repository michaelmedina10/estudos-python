# Funções decoradoras e decoradores
# Decorar = Adicionar | Remover | Restringir | Alterar
# Funções decoradoras são funções ue decoram outras funções
# Decoradores são usados para fazer o python usar as funções decoradores em outras funções
# Decoradores são sintaxe_sugar (Áçucar sintático) ou seja a linguagem tem recursos que facilitam o uso das funções decoradoras


## Eu ja tenho uma função que faz outras, uma factory, agr, posso ter uma função que cria decorators, pois
# assim eu poderei passar parametros por exemplo

def fabrica_de_decoradores(a=None, b=None, c=None):
    #1 função para receber parametros e ser visivel em todo esse scopo
    def fabrica_de_funcoes(func):
        #2 funçãp que recebe a função em si que quero executar
        print("fabricas_de_funcoes 1")
        def aninhada(*args, **kwargs):
            #3 quem recebe e executa em si a função passada a soma por exemplo
            print("Aninhada")
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


# Para aplicar a função criar_funcao podemos usar o decorator, funções iniciadas com @
# ao executar o decorator fabrica de decoradores
# ele vai até essa função, define ela, e retorna a closure fabrica de funções
# depois ele passa a função soma para dentro desse retorno como se fosse desse jeito
# fabrica_de_decoradores(a, b, c)(soma)
# entrando e definindo a função aninhada e retorna ela sem ser executada
# quando em alguma parte do código eu chamo a função soma, ele retorna para a função aninhada
# executa essa func com seus parametros
# ele vai até a função soma, processa, retorna, retorna para função aninhada e retorna para mim o valor da soma
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

# usando a função decoradoras sem a sintaxe do decorator
# inverte_string_checando_parametro = criar_funcao(inverte_string)
# string_invertida = inverte_string_checando_parametro(123)
# print(string_invertida)
resultado = soma(10, 10)

# Executando sem sintaxe_sugar
# multiplica_por_dez = fabrica_de_decoradores(1, 2, 3)(lambda x, y: x * y)
# print(multiplica_por_dez(5, 10))
# print(resultado)