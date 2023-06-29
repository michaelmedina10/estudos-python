# dir, hasattr e getattr serve para vc checar coisas dentro de um objeto

string = 'Michael'
metodo = 'upper'
print(dir(string)) # retorna os atributos dentro do objeto

if hasattr(string, metodo):
    print("EXISTE")
    # Parenteses para invocar o metodo
    print(getattr(string, metodo)())