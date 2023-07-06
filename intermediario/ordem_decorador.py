def parametros_decorador(nome=None):
    #1 função para receber parametros e ser visivel em todo esse scopo
    def decorador(func):
        #2 funçãp que recebe a função em si que quero executar
        print(f"Decorador: {nome}")
        def sua_nova_uncao(*args, **kwargs):
            #3 quem recebe e executa em si a função passada a soma por exemplo
            res = func(*args, **kwargs)
            print(res)
            res = f'{res} {nome}'
            return res
        return sua_nova_uncao
    return decorador


@parametros_decorador("Terceiro")
@parametros_decorador("Segundo")
@parametros_decorador("Primeiro")
def soma(x, y):
    # Passei varios parametros para a função soma por decorator, mas ele só executa uma vez a função em si a iteração é baseada nos
    # parametros recebidos
    print("executei")
    return x + y

resultado = soma(10, 10)
print(resultado)