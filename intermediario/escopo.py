'''
Existe o conceito de scopo global e local
global = todo código é visível e livre para acesso em seu módulo
local = somente o bloco em que a variável foi definida pode acessá-la
se eu criar uma variável x a nível global, fora de uma função ele será acessível em todo código, porém se eu tbm criar
uma variável x dentro de uma função, o que acontece, a busca irá procurar uma variável x primeiro no bloco em que se encontra
caso ache, a usará, caso contrário, irá abrangir sua busca para o próximo scopo, no nosso caso, o global direto.

blocos no python são definidos por identação, mas em linguagens como JavaScript são usadas as {}

{
global
    {
        local
        {
            local
        }
    }
}
'''

x = 1

def teste_scopo():

    x = 2
    print(x)

teste_scopo()
print(x)

# A palavra global faz com que a variável no scopo externo seja a mesma no interno

y = 2

def teste_global():

    global y
    y = 3
    print(y)

teste_global()
print(y)