
# String -> str -> tudo que esta entre aspas
# "ISSO É UMA STRING"
# "100" É UMA STRING


# TIPO DE TIPAGEM = Dinâmica / Forte

# Python infere o tipo de dado recebido em linguagens estáticas tu precisa colocar explicitamente o tipo
# string nome = 'texto'
# int idade = 26

print(type(100))
print(type("string"))
print(type(10.55))
print('Explícito', 'é', 'melhor " do que implícito')
# Tipagem forte
# Não converte automaticamente um tipo
# O Código abaixo resultaria no erro
# TypeError: can only concatenate str (not "int") to str
# print("Nome: Nao Sei, Idade: " + 10)



# Aspas Simples