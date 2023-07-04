def soma(x, y):
    return x + y

def multiplicar(x, y):
    return x * y

def criar_funcao(funcao, x):
    # Clojure, guardando em memória a execução de uma função, assim funciona como uma factory
    def interna(y):
        return funcao(x, y)
    return interna

# Posso criar funções a partir  da factory criar_funcao
soma_com_cinco = criar_funcao(soma, 5)
multiplicar_por_10 = criar_funcao(multiplicar, 10)
multiplicar_por_2 = criar_funcao(multiplicar, 2)

print(soma_com_cinco(5))
print(multiplicar_por_10(10))
print(multiplicar_por_2(2))